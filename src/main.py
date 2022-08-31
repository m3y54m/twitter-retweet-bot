import json
import pathlib
import bot
from server import start_server_thread

SRC_PATH = pathlib.Path(__file__).parent.resolve()
TRACK_JSON_PATH = SRC_PATH.joinpath("track.json")

MAX_RULES_COUNT = 25

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


if __name__ == "__main__":

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

        rulesList = create_rules_list(trackList, 512)
        rulesCount = len(rulesList)

        if (rulesCount > MAX_RULES_COUNT):
            print(
                f"\n[SimJowBot] [{bot.get_datetime()}] [WARNING] Number of required rules for the bot ({rulesCount}) is more than allowed ({MAX_RULES_COUNT})"
            )

        # keep the bot running in replit
        start_server_thread()

        # create a tweepy Stream object for real time filtering of latest posted tweets
        streamClient = bot.SimJowStream(bot.bearer_token, True)

        # Get a list of all rules registered on the bot's Twitter app
        rules = streamClient.get_rules().data
        ids = []
        if (rules):
            # Create the list of rule ids
            for rule in rules:
                ids.append(rule.id)
            # Delete all rules
            streamClient.delete_rules(ids)

        
        # Register the rules to the bot
        for i in range(MAX_RULES_COUNT):
            streamRule = bot.tweepy.StreamRule(rulesList[i])
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
