import os
from dotenv import load_dotenv
import tweepy

# take environment variables from .env.
load_dotenv()

# get environment variables for Twitter API
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth_url = auth.get_authorization_url()

# Open the link while signed in your desired bot account
print("Please authorize: " + auth_url)

# Get the 7-digit PIN code generated from the url
verifier = input("PIN: ").strip()

auth.get_access_token(verifier)

print("ACCESS_TOKEN = '%s'" % auth.access_token)
print("TOKEN_SECRET = '%s'" % auth.access_token_secret)
