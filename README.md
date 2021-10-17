# My Twitter API Playground

## Prerequisites

```console
pip install -r requirements.txt
```

## Examples

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