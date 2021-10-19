# SimJow Twitter Bot

[SimJow](https://twitter.com/SimJow) is a Twitter bot who looks for Persian tweets on the following topics and retweets them:

- Electronics Hardware Design
- Robotics
- Embedded Systems

## Prerequisites

```console
pip install -r requirements.txt
```

## Twitter API Examples

```console
curl -X GET -H "Authorization: Bearer <BEARER TOKEN>" "https://api.twitter.com/2/tweets/20"
```

```console
curl -X GET -H "Authorization: Bearer <BEARER TOKEN>" "https://api.twitter.com/2/tweets/20?expansions=author_id"
```

```console
curl -X GET -H "Authorization: Bearer <BEARER TOKEN>" "https://api.twitter.com/2/tweets/440322224407314432?expansions=author_id,attachments.media_keys"
```

```console
curl -X GET -H "Authorization: Bearer <BEARER TOKEN>" "https://api.twitter.com/2/tweets/1028039268030210048?expansions=author_id,attachments.poll_ids"
```

## Resources

- [Read key-value pairs from a .env file and set them as environment variables](https://github.com/theskumar/python-dotenv)
- [Hello Tweepy](https://docs.tweepy.org/en/v3.5.0/getting_started.html)
- [Post tweet with tweepy](https://stackoverflow.com/questions/19337672/post-tweet-with-tweepy)
- [Obtaining Access Tokens using 3-legged OAuth flow](https://developer.twitter.com/en/docs/authentication/oauth-1-0a/obtaining-user-access-tokens)
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