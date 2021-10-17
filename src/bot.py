import os
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

os.system(f'curl -X GET -H "Authorization: Bearer {bearer_token}" "https://api.twitter.com/2/tweets/20"')
print("")



# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()

# with open('timeline.txt', 'w') as f:
#     for tweet in public_tweets:
#         f.write(tweet.text + "\r\n")

# api.update_status(status="Hello World!")
