import json
import pathlib
import bot
from server import start_server_thread

SRC_PATH = pathlib.Path(__file__).parent.resolve()
TRACK_JSON_PATH = SRC_PATH.joinpath("track.json")

if __name__ == "__main__":

    with open(TRACK_JSON_PATH, "r") as trackJson:

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

        # keep the bot running in replit
        start_server_thread()

        # create a tweepy Stream object for real time filtering of latest posted tweets
        streamClient = bot.SimJowStream(bot.bearer_token, True)

        streamRuleString = '"ایران" lang:fa -is:retweet'

        streamRule = bot.tweepy.StreamRule(streamRuleString)
        streamClient.add_rules(streamRule)

        # To keep the bot running even if there is an error
        while True:

            print(
                f"\n[SimJowBot] [{bot.get_datetime()}] [INFO] Stream monitoring has started."
            )

            try:
                # start filtering the twitter stream in a loop
                streamClient.filter(
                    expansions=["author_id"],
                    user_fields=["username"],
                )
            except Exception as error:
                print(
                    f"\n[SimJowBot] [{bot.get_datetime()}] [ERROR] Something is wrong with tweets stream. Reason:\n{error}"
                )
