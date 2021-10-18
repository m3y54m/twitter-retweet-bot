import os
import time
from datetime import datetime
from flask import Flask
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


def get_date_time():
    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    return now.strftime("%Y/%m/%d %H:%M:%S")


app = Flask(__name__)


@app.route("/")
def home():
    twitterApi = bot.twitter_api_authenticate()
    userName, text = bot.get_tweet(twitterApi, 20)
    return f"{userName}: {text}"


if __name__ == "__main__":
    app.debug = False
    app.run(host="localhost", port=os.environ.get("PORT") or 3456)

    # # tweet interval in seconds
    # interval = 60

    # while True:

    #     twitterApi = bot.twitter_api_authenticate()
    #     text = (
    #         f"Consecutive Test Tweets at {interval} Seconds Interval:\n"
    #         + get_date_time()
    #     )

    #     bot.post_tweet(twitterApi, text)
    #     # wait for the interval
    #     time.sleep(interval)
