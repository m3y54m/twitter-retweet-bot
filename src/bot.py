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


# os.system(f'curl -X GET -H "Authorization: Bearer {bearer_token}" "https://api.twitter.com/2/tweets/20"')
# print("")

def tweet_hello_world():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    api.update_status(status="Hello World from Bot!")

def get_tweet_text(tweetId):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    status = api.get_status(id=tweetId)
    return status.user.name, status.text

def get_timeline():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    public_tweets = api.home_timeline()
    timeline_list=[]
    for tweet in public_tweets:
        timeline_list.append(tweet.text)
    return timeline_list

    
# public_tweets = api.home_timeline()

# with open('timeline.txt', 'w') as f:
#     for tweet in public_tweets:
#         f.write(tweet.text + "\r\n")

if __name__ == "__main__":
    # username, text = get_tweet_text(20)
    # print(f"{username}: {text}")

    print(get_timeline())