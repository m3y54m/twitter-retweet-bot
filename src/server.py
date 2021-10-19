import os
from flask import Flask
from flask import Response
from dotenv import load_dotenv

# import bot.py
try:
    # suitable for heroku
    from . import bot
except:
    # suitable for local development
    import bot

# take environment variables from .env.
load_dotenv()


app = Flask(__name__)


@app.route("/")
def home():
    twitterApi = bot.twitter_api_authenticate()
    userName, text = bot.get_tweet(twitterApi, 20)
    return f"{userName}: {text}"


# Wake my Heroku dyno by wakemydyno.com
@app.route("/wakemydyno.txt")
def get_text():
    content = "God bless Heroku!"
    return Response(content, mimetype="text/plain")


if __name__ == "__main__":
    app.debug = False
    app.run(host="localhost", port=os.environ.get("PORT") or 3456)
