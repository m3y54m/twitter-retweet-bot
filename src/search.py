import os
import tweepy
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
bot_username = "SimJow"

import json
import pathlib
import bot

SRC_PATH = pathlib.Path(__file__).parent.resolve()
TRACK_JSON_PATH = SRC_PATH.joinpath("track.json")

MAX_RULES_COUNT = 25
MAX_RULE_LENGTH = 512


def create_rules_list(keywordsList, ruleMaxLength):
    keywordsListSize = len(keywordsList)
    ruleInitial = f"lang:fa -is:retweet -is:reply -from:{bot.bot_username} -retweets_of:{bot.bot_username} ("
    rule = ruleInitial
    ruleSize = len(rule)
    rulesList = []
    portionsCount = 0

    if ruleSize < ruleMaxLength:
        # Iterate over keywords until the one before the last item
        for i in range(keywordsListSize - 1):

            # Get two consecutive items from list
            currentKeywordString = f'"{keywordsList[i]}" OR '
            currentKeywordStringLast = f'"{keywordsList[i]}")'
            nextKeywordStringLast = f'"{keywordsList[i+1]}")'

            ck = len(currentKeywordString)
            ckl = len(currentKeywordStringLast)
            nkl = len(nextKeywordStringLast)
            ruleSize = len(rule)

            if i < keywordsListSize - 2:
                if ruleSize + ck + nkl < ruleMaxLength:
                    rule += currentKeywordString
                    # Continue until portion is full
                elif ruleSize + ck + nkl == ruleMaxLength:
                    rule += currentKeywordString + nextKeywordStringLast
                    rulesList.append(rule)
                    portionsCount += 1
                    rule = ruleInitial
                elif (
                    ruleSize + ck + nkl > ruleMaxLength
                    and ruleSize + ckl <= ruleMaxLength
                ):
                    rule += currentKeywordStringLast
                    rulesList.append(rule)
                    portionsCount += 1
                    rule = ruleInitial
            else:  # if (i == keywordsListSize - 2)
                if ruleSize + ck + nkl <= ruleMaxLength:
                    rule += currentKeywordString + nextKeywordStringLast
                    rulesList.append(rule)
                    portionsCount += 1
                    # Finish

    return rulesList


with open(TRACK_JSON_PATH, "r", encoding="utf-8") as trackJson:

    trackDic = json.load(trackJson)

    keywordsList = trackDic["keywords"]
    hashtagsList = trackDic["hashtags"]
    mentionsList = trackDic["mentions"]

    trackList = []
    # Add keywords to track list
    trackList.extend(keywordsList)
    # Add hashtags to track list
    trackList.extend(hashtagsList)
    # Add mentions to track list
    # trackList.extend(mentionsList)

    rulesList = create_rules_list(trackList, MAX_RULE_LENGTH)
    rulesCount = len(rulesList)
    print(rulesCount)

    client = tweepy.Client(bearer_token)

    # Search Recent Tweets
    start_time = "2022-09-01T15:25:00.000Z"

    for i in range(rulesCount):
        # This endpoint/method returns Tweets from the last seven days
        # By default, this endpoint/method returns 10 results
        # You can retrieve up to 100 Tweets by specifying max_results
        response = client.search_recent_tweets(
            rulesList[i],
            expansions=["author_id"],
            user_fields=["id", "username"],
            start_time=start_time,
            max_results=100,
        )
        # The method returns a Response object, a named tuple with data, includes,
        # errors, and meta fields
        print(response.meta)

        # In this case, the data field of the Response returned is a list of Tweet
        # objects
        tweets = response.data

        # You can then access those objects in the includes Response field
        includes = response.includes
        users = includes["users"]

        # An efficient way of matching expanded objects to each data object is to
        # create a dictionary of each type of expanded object, with IDs as keys
        users = {user["id"]: user for user in users}
        for tweet in tweets:
            print(
                f"\n[SimJowBot] [{bot.get_datetime()}] [INFO] Found a matching tweet https://twitter.com/{users[tweet.author_id].username}/status/{tweet.id} "
            )
