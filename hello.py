import os
from flask import Flask
from dotenv import load_dotenv
# take environment variables from .env.
load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World from Flask!"


app.run()
