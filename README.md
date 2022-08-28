# SimJow Twitter Bot

[SimJow](https://twitter.com/SimJow) is a Twitter bot who looks for Persian tweets on the following topics and retweets them:

- Electronics Hardware Design
- Embedded Systems
- Computer Hardware
- Robotics

## Prerequisites

First you should (or it is recommended to) install [Poetry](https://python-poetry.org/) for package management:

```console
pip install poetry
```

Then install all the required packages based on `poetry.lock` file using this command:

```console
poetry install
```

To update all packages use this command:

```console
poetry update
```

## Run the bot

```console
python src/main.py
```

## Project Strcture

This robot simply uses keywords in `src/track.json` file to find desired tweets.

The main source file which controls the behavior of robot is `src/bot.py`.

## Development Resources

- [Read key-value pairs from a .env file and set them as environment variables](https://github.com/theskumar/python-dotenv)
- [Hello Tweepy](https://docs.tweepy.org/en/stable/getting_started.html)
- [Post tweet with tweepy](https://stackoverflow.com/questions/19337672/post-tweet-with-tweepy)
- [Obtaining Access Tokens using 3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
- [tweepy.Stream — Stream Reference](https://docs.tweepy.org/en/stable/stream.html)
- [How to Make a Twitter Bot in Python With Tweepy](https://realpython.com/twitter-bot-python-tweepy)
- [Getting Started With Flask, A Python Microframework](https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework)
- [A hello world app in Flask for deploying to Heroku.](https://github.com/leah/hello-flask-heroku)
- [Tweet Quote Bot](https://github.com/adamichelle/tweet-quote-bot)
- [tweepy unauthorized 401 error when retweeting](https://stackoverflow.com/questions/69563386/tweepy-unauthorized-401-error-when-retweeting)
- [Relative imports - ModuleNotFoundError: No module named x](https://stackoverflow.com/questions/43728431/relative-imports-modulenotfounderror-no-module-named-x)
- [Heroku: The Procfile](https://devcenter.heroku.com/articles/procfile)
- [Twitter Retweet Bot using Python & Tweepy](https://github.com/0xGrimnir/Simple-Retweet-Bot)
- [Wake my Dyno!](http://wakemydyno.com/)
- [How do I allow a file to be viewed?](https://askto.pro/question/how-do-i-allow-a-file-to-be-viewed)
- [Filter realtime Tweets](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/filter-realtime/guides/basic-stream-parameters)
- [Building a Discord Bot with Python and Repl.it](https://www.codementor.io/@garethdwyer/building-a-discord-bot-with-python-and-repl-it-miblcwejz#keeping-our-bot-alive)
- [GitHub Webhooks](https://docs.github.com/en/developers/webhooks-and-events/webhooks)
- [Verify GitHub webhook request sha256 in PHP](https://gist.github.com/mahdyar/711beee9fec9cab6bb2f6e48d061d077)
- [Stream encountered HTTP error: 403](https://stackoverflow.com/questions/70031766/receiving-stream-encountered-http-error-403-when-using-twitter-api-what-is-c)
- [PIN-based authorization](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/pin-based-oauth)
- [Twitter API V2 Programming with Python and Tweepy](https://python.plainenglish.io/twitter-api-v2-programming-with-python-and-tweepy-f6487cd4bad9)