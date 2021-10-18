import os
import time
from datetime import datetime
import tweepy
from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv()

# get environment variables for Twitter API
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
bearer_token = os.environ.get("BEARER_TOKEN")


def twitter_api_authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except Exception as error:
        print(
            f"\n[ SimJowBot ] An error occurred while attempting to authenticate with the twitter API. Reason:\n{error}"
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
                f"\n[ SimJowBot ] An error occurred while attempting to get the twitter status with id={tweetId}. Reason:\n{error}"
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
                f"\n[ SimJowBot ] An error occurred while attempting to update the twitter status. Reason:\n{error}"
            )
        else:
            success = True

    return success


def get_date_time():
    # datetime object containing current date and time
    now = datetime.now()
    # YY/mm/dd H:M:S
    return now.strftime("%Y/%m/%d %H:%M:%S")


def loop_for_tweets(intervalSeconds):

    twitterApi = twitter_api_authenticate()

    while True:
        text = (
            f"Consecutive Test Tweets at {intervalSeconds} Seconds Intervals:\n"
            + get_date_time()
        )
        # post the tweet to Twitter
        post_tweet(twitterApi, text)
        # wait for the interval
        time.sleep(intervalSeconds)


if __name__ == "__main__":
    # tweet interval in seconds
    interval = 10
    #loop_for_tweets(interval)

    twitterApi = twitter_api_authenticate()

    for tweet in tweepy.Cursor(twitterApi.search_tweets, q="#الکترونیک OR #رباتیک").items(5):

        print(f"\n[ SimJowBot ] Retweet Bot found tweet by @{tweet.user.screen_name}. Attempting to retweet.")
        try:
            # Like the tweet
            twitterApi.create_favorite(tweet.id)
            # Retweet the tweet
            twitterApi.retweet(tweet.id)
        # Some basic error handling. Will print out why retweet failed, into your terminal.
        except Exception as error:
            print(f"\n[ SimJowBot ] ERROR: Retweet not successful. Reason:\n{error}")
        except StopIteration:
            break
        else:
            print(f"\n[ SimJowBot ] Retweet published successfully.")
        
        # Where sleep(10), sleep is measured in seconds.
        # Change 10 to amount of seconds you want to have in-between retweets.
        # Read Twitter's rules on automation. Don't spam!
        time.sleep(interval)

