import os
from flask import Flask
from dotenv import load_dotenv
# take environment variables from .env.
load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    # bot.tweet_quote()
    return "Hello World from Flask!"


app.run(host="127.0.0.1", port=os.environ.get("PORT") or 3456)
