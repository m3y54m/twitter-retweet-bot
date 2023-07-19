import my_twitter_bot as bot

twitterClient = bot.twitter_api_authenticate_v2()
bot.post_tweet_v2(twitterClient, "یک دو سه آزمایش می‌کنیم...")