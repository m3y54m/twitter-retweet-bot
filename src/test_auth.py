import tweepy
import os
from dotenv import load_dotenv

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


def twitter_api_authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
    except Exception as error:
        print(
            f"\n[ERROR] Unable to authenticate with the twitter API. Reason:\n{error}"
        )
        return None
    else:
        print(f"\n[INFO] Authentication successful.")
        return api


def twitter_api_authenticate_v2():
    return tweepy.Client(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
        wait_on_rate_limit=True,
    )


def create_test_tweet_v2(client):
    response = client.create_tweet(text="This Tweet is for test!")
    print(f"https://twitter.com/user/status/{response.data['id']}")


client = twitter_api_authenticate_v2()
# print(client.get_user(username="twitter"))
# Post a test Tweet
# create_test_tweet_v2(client)
