import os
from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv()

# get environment variable BEARER_TOKEN
bearer_token = os.environ.get("BEARER_TOKEN")

# use curl to get tweet data
os.system(f'curl -X GET -H "Authorization: Bearer {bearer_token}" "https://api.twitter.com/2/tweets/20"')
print("")

