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
    twitterClient = bot.twitter_api_authenticate_v2()
    userName, text = bot.get_tweet_v2(twitterClient, 20)
    return Response(f"{userName}: {text}", mimetype="text/plain")


# Wake up my bot
@app.route("/wakeup")
def wakeup():
    return Response("👀", mimetype="text/plain")


def run():
    from waitress import serve
    serve(app, host="0.0.0.0", port=os.environ.get("PORT") or 8080)


def start_server_thread():
    t = Thread(target=run)
    t.start()
