import os
from dotenv import dotenv_values

# search in increasingly higher folders for the ".env" file
config = dotenv_values(".env") 

# print all environments variables defined in ".env"
for key, value in config.items():
    print(key, value)

# use curl to get tweet data
os.system(f'curl -X GET -H "Authorization: Bearer {config["BEARER_TOKEN"]}" "https://api.twitter.com/2/tweets/20"')
print("")

