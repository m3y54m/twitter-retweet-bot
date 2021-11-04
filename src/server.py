import os
from flask import Flask
from flask import Response
from dotenv import load_dotenv
from threading import Thread

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
    content = "I'm alive!"
    return Response(content, mimetype="text/plain")


def run():
    app.run(host='0.0.0.0', port=os.environ.get("PORT") or 8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
