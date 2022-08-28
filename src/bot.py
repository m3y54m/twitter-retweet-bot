import os
import tweepy
from dotenv import load_dotenv
from datetime import datetime

# take environment variables from .env.
load_dotenv()

# get environment variables for Twitter API
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
bearer_token = os.environ.get("BEARER_TOKEN")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
bot_username = "SimJow"

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


def twitter_api_authenticate_v2():
    return tweepy.Client(consumer_key=consumer_key,
                         consumer_secret=consumer_secret,
                         access_token=access_token,
                         access_token_secret=access_token_secret,
                         wait_on_rate_limit=True)


def get_tweet(twitterClient, tweetId):
    userName = None
    tweetText = None

    if twitterClient:
        try:
            status = twitterClient.get_status(id=tweetId)
        except Exception as error:
            print(
                f"\n[SimJowBot] [{get_datetime()}] [ERROR] Unable to get the twitter status with id={tweetId}. Reason:\n{error}"
            )
        else:
            userName = status.user.name
            tweetText = status.text

    return userName, tweetText


def get_tweet_v2(client, tweetId):
    userName = None
    tweetText = None

    if client:
        try:
            tweet = client.get_tweet(id=tweetId,
                                     expansions=["author_id"],
                                     user_fields=["name"],
                                     user_auth=True)
        except Exception as error:
            print(
                f"\n[SimJowBot] [{get_datetime()}] [ERROR] Unable to get the tweet with id={tweetId}. Reason:\n{error}"
            )
        else:
            tweetText = tweet.data.text
            userName = tweet.includes["users"][0].name

    return userName, tweetText


def post_tweet(twitterClient, tweetText):
    success = False

    if twitterClient:
        try:
            twitterClient.update_status(status=tweetText)
        except Exception as error:
            print(
                f"\n[SimJowBot] [{get_datetime()}] [ERROR] Unable to update the twitter status. Reason:\n{error}"
            )
        else:
            success = True

    return success


class SimJowStream(tweepy.StreamingClient):
    def __init__(self, bearer_token, wait_on_rate_limit):
        super().__init__(bearer_token=bearer_token,
                         wait_on_rate_limit=wait_on_rate_limit)
        self.twitterClient = twitter_api_authenticate_v2()
        self.myUser = self.twitterClient.get_user(username=bot_username,
                                                  user_auth=True)
        print(
            f"\n[SimJowBot] [{get_datetime()}] [INFO] Initialized the Twitter stream monitoring agent."
        )

    # when a new tweet is posted on Twitter with your filtered specifications
    def on_response(self, response):

        # print(response.data.id)
        # tweetText = tweet.data.text
        # userName = tweet.includes["users"][0].name

        print(
            f"\n[SimJowBot] [{get_datetime()}] [INFO] Found a matching tweet https://twitter.com/{response.includes['users'][0].username}/status/{response.data.id} "
       )

        # # If the found tweet is suitable to retweet
        # if self.is_suitable_to_retweet(status):
        #     # Retweet the found tweet (status)
        #     self.retweet(status)
        #     # Like the found tweet (status)
        #     self.like(status)

    def retweet(self, status):
        try:
            # Retweet the tweet
            self.twitterClient.retweet(status.id)
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
            self.twitterClient.create_favorite(status.id)
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

        blockedIdsList = self.twitterClient.get_blocked_ids()
        mutedIdsList = self.twitterClient.get_muted_ids()

        if hasattr(status, "retweeted_status"):
            # Check the original tweet if it was a retweet
            originalStatus = self.twitterClient.get_status(
                id=status.retweeted_status.id)

            isReply = originalStatus.in_reply_to_status_id is not None
            isAuthorBlocked = originalStatus.user.id in blockedIdsList
            isAuthorMuted = originalStatus.user.id in mutedIdsList
            isAuthorMyself = originalStatus.user.screen_name == self.myUser.screen_name
            isRetweetedByMyself = status.user.screen_name == self.myUser.screen_name
        else:
            # Check the tweet itself
            isReply = status.in_reply_to_status_id is not None
            isAuthorBlocked = status.user.id in blockedIdsList
            isAuthorMuted = status.user.id in mutedIdsList
            isAuthorMyself = status.user.screen_name == self.myUser.screen_name
            isRetweetedByMyself = False

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
        elif isAuthorMuted:
            print(
                f"[SimJowBot] [{get_datetime()}] [WARN] Tweet is not suitable. Reason: Author is muted."
            )
            return False
        elif isAuthorMyself:
            print(
                f"[SimJowBot] [{get_datetime()}] [WARN] Tweet is not suitable. Reason: Author is myself."
            )
            return False
        elif isRetweetedByMyself:
            print(
                f"[SimJowBot] [{get_datetime()}] [WARN] Tweet is not suitable. Reason: Retweeted previously by myself."
            )
            return False
        else:
            return True
