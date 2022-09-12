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

Install all the required packages based on `poetry.lock` using this command:

```console
poetry install
```

To update all packages to their latest versions you can use this command:

```console
poetry update
```

Convert `poetry.lock` to `requirements.txt`:

```console
poetry export -f requirements.txt --output requirements.txt
```

## Run the bot

```console
python src/main.py
```

## Project Strcture

### `src/track.json`

This bot simply uses keywords in this file to find desired tweets.
This file consists of two parts:
- `include`: All keywords, hashtags, and mentions that should exist in the tweets bot is looking for.
- `exclude`: All keywords, hashtags, and mentions that should **NOT** exist in the tweets.

### `src/main.py`

This is the entry point of the program. It Gets keywords from `src/track.json` and processes them and
generates valid search rules for out Twitter bot. It also runs a Flask web server to monitor or control
the bot's activity. Finally it runs the bot's main application.

### `src/bot.py`

This file defines the application and behavior of this Twitter bot.
It is using Twitter API v2 StreamingClient to monitor Twitter live steam of tweets
based on the rules defined for it.

Currently the bot only likes and retweets the tweets that match the rules. 

### `src/server.py`

A Flask web server is run to monitor or control the bots activity.

### `src/get_access_token.py`

This file is a independent utility to generate user-specific access tokens for the bot's Twitter API app
and the bot's functionality is not related to this file.


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
- [POST /2/tweets/search/stream/rules](https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/api-reference/post-tweets-search-stream-rules#tab0)
- [Invalid Rules Problem](https://developer.twitter.com/en/support/twitter-api/error-troubleshooting#invalid-rules)
- [Deploy on Fly.io](https://fly.io/docs/getting-started/python/)