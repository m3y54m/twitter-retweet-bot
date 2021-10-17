import os
from flask import Flask
from dotenv import load_dotenv
import bot

# take environment variables from .env.
load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    bot.tweet_hello_world()
    return "Hello World from Flask!"

if __name__ == "__main__":
    app.run(host="localhost", port=os.environ.get("PORT") or 3456)
