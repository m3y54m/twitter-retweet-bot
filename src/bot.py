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
    # interval = 60
    # loop_for_tweets(interval)

    twitterApi = twitter_api_authenticate()
    # First Persian tweet
    post_tweet(twitterApi, "اولین توییت فارسی سیم‌جُو!")
