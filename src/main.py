import json
import pathlib
import bot
from server import start_server_thread

SRC_PATH = pathlib.Path(__file__).parent.resolve()
TRACK_JSON_PATH = SRC_PATH.joinpath("track.json")

MAX_RULES_COUNT = 25
MAX_RULE_LENGTH = 512


def create_rules_list(includeList, excludeList, ruleMaxLength):
    includeListSize = len(includeList)
    ruleInitial = f"lang:fa -is:retweet -is:reply -from:{bot.bot_username} -retweets_of:{bot.bot_username}"
    rulesList = []
    portionsCount = 0

    # Add exclude list keywords to each rule
    if len(ruleInitial) < ruleMaxLength:
        excludeString = " ".join(f'-"{k}"' for k in excludeList)
        ruleInitial += " " + excludeString + " ("
        rule = ruleInitial
    else:
        print(
            f"\n[SimJowBot] [{bot.get_datetime()}] [ERROR] Initial rule string is longer than allowed."
        )

    if len(rule) < ruleMaxLength:
        # Iterate over keywords until the one before the last item
        for i in range(includeListSize - 1):

            # Get two consecutive items from list
            currentKeywordString = f'"{includeList[i]}" OR '
            currentKeywordStringLast = f'"{includeList[i]}")'
            nextKeywordStringLast = f'"{includeList[i+1]}")'

            ck = len(currentKeywordString)
            ckl = len(currentKeywordStringLast)
            nkl = len(nextKeywordStringLast)
            ruleSize = len(rule)

            if i < includeListSize - 2:
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
            else:  # if (i == includeListSize - 2)
                if ruleSize + ck + nkl <= ruleMaxLength:
                    rule += currentKeywordString + nextKeywordStringLast
                    rulesList.append(rule)
                    portionsCount += 1
                    # Finish
    else:
        print(
            f"\n[SimJowBot] [{bot.get_datetime()}] [ERROR] Rule string after adding exclude list is longer than allowed."
        )

    return rulesList


if __name__ == "__main__":

    includeList = []
    excludeList = []

    with open(TRACK_JSON_PATH, "r", encoding="utf-8") as trackJson:

        try:
            fileContents = trackJson.read()
            # Remove all ZERO WIDTH NON-JOINER (‌U+200C) characters (Ctrl + Shift + 2)
            # because Twitter API v2 rules don't support it
            fileContents = fileContents.replace("\u200c", "")

            # Convert JSON string to Python dictionary
            trackDic = json.loads(fileContents)

            # Create list of keywords should be included in twitter search query (rule)
            keywordsList = trackDic["include"]["keywords"]
            hashtagsList = trackDic["include"]["hashtags"]
            mentionsList = trackDic["include"]["mentions"]
            # Add keywords to track list
            includeList.extend(keywordsList)
            # Add hashtags to track list
            includeList.extend(hashtagsList)
            # Add mentions to track list
            includeList.extend(mentionsList)

            # print(includeList)

            # Create list of keywords should be excluded from twitter search query (rule)
            keywordsList = trackDic["exclude"]["keywords"]
            hashtagsList = trackDic["exclude"]["hashtags"]
            mentionsList = trackDic["exclude"]["mentions"]
            # Add keywords to track list
            excludeList.extend(keywordsList)
            # Add hashtags to track list
            excludeList.extend(hashtagsList)
            # Add mentions to track list
            excludeList.extend(mentionsList)

            # print(excludeList)

        except Exception as error:
            print(
                f"\n[SimJowBot] [{bot.get_datetime()}] [ERROR] Keywords list generation failed. Reason:\n{error}"
            )

        # if len(includeList) != 0:
        #     rulesList = create_rules_list(includeList, excludeList, MAX_RULE_LENGTH)
        #     rulesCount = len(rulesList)
        #     if rulesCount == 0:
        #         raise Exception(
        #             f"\n[SimJowBot] [{bot.get_datetime()}] [ERROR] No rule string is generated!"
        #         )
        #     print(f"Total rule strings generates: {rulesCount}\n")
        #     for index, ruleStr in enumerate(rulesList):
        #         print(f"Rule string {index+1}:\n{ruleStr}\n")
        # else:
        #     raise Exception(
        #         f"\n[SimJowBot] [{bot.get_datetime()}] [ERROR] Keywords include list is empty."
        #     )

        # if rulesCount > MAX_RULES_COUNT:
        #     print(
        #         f"\n[SimJowBot] [{bot.get_datetime()}] [WARNING] Number of required rules for the bot ({rulesCount}) is more than allowed ({MAX_RULES_COUNT})"
        #     )

        # # keep the bot running in replit
        # start_server_thread()

        # # create a tweepy Stream object for real time filtering of latest posted tweets
        # streamClient = bot.SimJowStream(bot.bearer_token, True)

        # # Get a list of all rules registered on the bot's Twitter app
        # rules = streamClient.get_rules().data
        # ids = []
        # if rules:
        #     # Create the list of rule ids
        #     for rule in rules:
        #         ids.append(rule.id)
        #     # Delete all rules
        #     streamClient.delete_rules(ids)

        # # Register the rules to the bot
        # streamRulesList = []
        # print("\nCreating rules...\n")
        # for i in range(min(rulesCount, MAX_RULES_COUNT)):
        #     streamRule = bot.tweepy.StreamRule(rulesList[i])
        #     streamRulesList.append(streamRule)

        # rsp = streamClient.add_rules(add=streamRulesList)

        # if rsp.meta is not None:
        #     print(
        #         f"Rules created: {rsp.meta['summary']['created']}\nRules not created: {rsp.meta['summary']['not_created']}\nValid rules: {rsp.meta['summary']['valid']}\nInvalid rules: {rsp.meta['summary']['invalid']}\n"
        #     )

        # if rsp.data is not None:
        #     print("\nDATA:")
        #     print(rsp.data)

        # if rsp.errors is not None:
        #     print("\nERRORS:")
        #     print(rsp.errors)

        # # To keep the bot running even if there is an error
        # while True:

        #     print(
        #         f"\n[SimJowBot] [{bot.get_datetime()}] [INFO] Stream monitoring has started."
        #     )

        #     try:
        #         # start filtering the twitter stream in a loop
        #         streamClient.filter(
        #             expansions=["author_id"],
        #             user_fields=["id", "username"],
        #         )
        #     except Exception as error:
        #         print(
        #             f"\n[SimJowBot] [{bot.get_datetime()}] [ERROR] Something is wrong with tweets stream. Reason:\n{error}"
        #         )
