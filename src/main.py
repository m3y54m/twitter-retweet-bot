from dotenv import dotenv_values

# search in increasingly higher folders for the ".env" file
config = dotenv_values(".env") 

# print all environments variables defined in ".env"
for key, value in config.items():
    print(key, value)


