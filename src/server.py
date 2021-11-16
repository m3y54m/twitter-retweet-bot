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
    return Response(f"{userName}: {text}", mimetype="text/plain")


# Wake up my bot
@app.route("/wakeup")
def wakeup():
    return Response("👀", mimetype="text/plain")


def run():
    app.run(host='0.0.0.0', port=os.environ.get("PORT") or 8080)


def start_server_thread():
    t = Thread(target=run)
    t.start()
