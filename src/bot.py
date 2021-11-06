import os
import tweepy
from dotenv import load_dotenv
from datetime import datetime

# take environment variables from .env.
load_dotenv()

# get environment variables for Twitter API
consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
bearer_token = os.environ["BEARER_TOKEN"]


def get_datetime():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def twitter_api_authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
    except Exception as error:
        print(
            f"\n[SimJowBot] [{get_datetime()}] [ERROR] Unable to authenticate with the twitter API. Reason:\n{error}"
        )
        return None
    else:
        return api


def get_tweet(twitterApi, tweetId):
    userName = None
    tweetText = None

    if twitterApi:
        try:
            status = twitterApi.get_status(id=tweetId)
        except Exception as error:
            print(
                f"\n[SimJowBot] [{get_datetime()}] [ERROR] Unable to get the twitter status with id={tweetId}. Reason:\n{error}"
            )
        else:
            userName = status.user.name
            tweetText = status.text

    return userName, tweetText


def post_tweet(twitterApi, tweetText):
    success = False

    if twitterApi:
        try:
            twitterApi.update_status(status=tweetText)
        except Exception as error:
            print(
                f"\n[SimJowBot] [{get_datetime()}] [ERROR] Unable to update the twitter status. Reason:\n{error}"
            )
        else:
            success = True

    return success


class SimJowStream(tweepy.Stream):
    def __init__(self, consumer_key, consumer_secret, access_token,
                 access_token_secret):
        super().__init__(consumer_key, consumer_secret, access_token,
                         access_token_secret)
        self.twitterApi = twitter_api_authenticate()
        self.myUser = self.twitterApi.get_user(screen_name="SimJow")
        print(f"\n[SimJowBot] [{get_datetime()}] [INFO] SimJow is running.")

    # when a new tweet is posted on Twitter with your filtered specifications
    def on_status(self, status):

        print(
            f"\n[SimJowBot] [{get_datetime()}] [INFO] Found a matching tweet https://twitter.com/{status.user.screen_name}/status/{status.id} "
        )

        # If the found tweet is suitable to retweet
        if self.is_suitable_to_retweet(status):
            # Retweet the found tweet (status)
            self.retweet(status)
            # Like the found tweet (status)
            self.like(status)

    def retweet(self, status):
        try:
            # Retweet the tweet
            self.twitterApi.retweet(status.id)
        # Some basic error handling. Will print out why retweet failed, into your terminal.
        except Exception as error:
            print(
                f"[SimJowBot] [{get_datetime()}] [ERROR] Retweet was not successful. Reason:\n{error}"
            )
        else:
            print(
                f"[SimJowBot] [{get_datetime()}] [INFO] Retweeted successfully."
            )

    def like(self, status):
        try:
            # Like the tweet
            self.twitterApi.create_favorite(status.id)
        # Some basic error handling. Will print out why favorite failed, into your terminal.
        except Exception as error:
            print(
                f"[SimJowBot] [{get_datetime()}] [ERROR] Favorite was not successful. Reason:\n{error}"
            )
        else:
            print(
                f"[SimJowBot] [{get_datetime()}] [INFO] Favorited successfully."
            )

    def is_suitable_to_retweet(self, status):

        blockedIdsList = self.twitterApi.get_blocked_ids()

        if hasattr(status, "retweeted_status"):
            # Check the original tweet if it was a retweet
            originalStatus = self.twitterApi.get_status(
                id=status.retweeted_status.id)

            isReply = originalStatus.in_reply_to_status_id is not None
            isAuthorBlocked = originalStatus.user.id in blockedIdsList
            isAuthorMyself = originalStatus.user.screen_name == self.myUser.screen_name
        else:
            # Check the tweet itself
            isReply = status.in_reply_to_status_id is not None
            isAuthorBlocked = status.user.id in blockedIdsList
            isAuthorMyself = status.user.screen_name == self.myUser.screen_name

        if isReply:
            print(
                f"[SimJowBot] [{get_datetime()}] [WARN] Tweet is not suitable. Reason: It is a reply."
            )
            return False
        elif isAuthorBlocked:
            print(
                f"[SimJowBot] [{get_datetime()}] [WARN] Tweet is not suitable. Reason: Author is blocked."
            )
            return False
        elif isAuthorMyself:
            print(
                f"[SimJowBot] [{get_datetime()}] [WARN] Tweet is not suitable. Reason: Author is myself."
            )
            return False
        else:
            return True
