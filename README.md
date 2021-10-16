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

