import os
from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv()

# get environment variables for Twitter API
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
token_secret = os.environ.get("TOKEN_SECRET")
bearer_token = os.environ.get("BEARER_TOKEN")

# use curl to get tweet data
os.system(f'curl -X GET -H "Authorization: Bearer {bearer_token}" "https://api.twitter.com/2/tweets/20"')
print("")

