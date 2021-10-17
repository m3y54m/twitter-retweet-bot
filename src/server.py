import os
import tweepy
from flask import Flask
from dotenv import load_dotenv


# take environment variables from .env.
load_dotenv()

# get environment variables for Twitter API
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
bearer_token = os.environ.get("BEARER_TOKEN")

def get_tweet_text(tweetId):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    status = api.get_status(id=tweetId)
    return status.user.name, status.text


app = Flask(__name__)


@app.route("/")
def home():
    #bot.tweet_hello_world()
    username, text = get_tweet_text(20)
    return f"{username}: {text}"

if __name__ == "__main__":
    app.run(host="localhost", port=os.environ.get("PORT") or 3456)
