import os
import time
from datetime import datetime
import tweepy
from dotenv import load_dotenv

# take environment variables from .env.
load_dotenv()

# get environment variables for Twitter API
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
bearer_token = os.environ.get("BEARER_TOKEN")


def twitter_api_authenticate():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    try:
        api.verify_credentials()
    except Exception as error:
        print(
            f"\n[ SimJowBot ] An error occurred while attempting to authenticate with the twitter API. Reason:\n{error}"
        )
        return None
    else:
        return api


def get_tweet(twitterApi, tweetId):
    userName = None
    tweetText = None

    if twitterApi:
        try:
            status = twitterApi.get_status(id=tweetId)
        except Exception as error:
            print(
                f"\n[ SimJowBot ] An error occurred while attempting to get the twitter status with id={tweetId}. Reason:\n{error}"
            )
        else:
            userName = status.user.name
            tweetText = status.text

    return userName, tweetText


def post_tweet(twitterApi, tweetText):
    success = False

    if twitterApi:
        try:
            twitterApi.update_status(status=tweetText)
        except Exception as error:
            print(
                f"\n[ SimJowBot ] An error occurred while attempting to update the twitter status. Reason:\n{error}"
            )
        else:
            success = True

    return success


class SimJowStream(tweepy.Stream):
    def __init__(
        self, consumer_key, consumer_secret, access_token, access_token_secret
    ):
        super().__init__(
            consumer_key, consumer_secret, access_token, access_token_secret
        )

        self.twitterApi = twitter_api_authenticate()
        self.myUser = self.twitterApi.get_user(screen_name="SimJow")

    # when a new tweet is posted on Twitter with your filtered specifications
    def on_status(self, status):
        # If the user is not myself
        if status.user.screen_name != self.myUser.screen_name:

            print(
                f"\n[ SimJowBot ] Found a matching tweet https://twitter.com/{status.user.screen_name}/status/{status.id} "
            )
            # Retweet the found tweet (status)
            self.retweet(status)
            # Like the found tweet (status)
            self.like(status)

    def retweet(self, status):
        try:
            # Retweet the tweet
            self.twitterApi.retweet(status.id)
        # Some basic error handling. Will print out why retweet failed, into your terminal.
        except Exception as error:
            print(f"[ SimJowBot ] ERROR: Retweet was not successful. Reason:\n{error}")
        else:
            print(f"[ SimJowBot ] Retweeted successfully.")

    def like(self, status):
        try:
            # Like the tweet
            self.twitterApi.create_favorite(status.id)
        # Some basic error handling. Will print out why retweet failed, into your terminal.
        except Exception as error:
            print(f"[ SimJowBot ] ERROR: Favorite was not successful. Reason:\n{error}")
        else:
            print(f"[ SimJowBot ] Favorited successfully.")


if __name__ == "__main__":

    keywordsList = [
        "مهندسی الکترونیک",
        "بورد الکترونیکی",
        "مدار الکترونیکی",
        "برد الکترونیکی",
        "سخت افزار کامپیوتر",
        "سخت‌افزار کامپیوتر",
        "معماری کامپیوتر",
        "رباتیک",
        "ربات",
        "مکاترونیک",
        "امبدد",
        "سیستم های نهفته",
        "سیستم های توکار",
        "سیستم‌های نهفته",
        "سیستم‌های توکار",
        "Arduino",
        "آردوینو",
        "Raspberry Pi",
        "Digilent",
        "دیجیلنت",
        "رزبری پای",
        "رزپری پای",
        "رسپری پای",
        "رزبری‌پای",
        "رزپری‌پای",
        "رسپری‌پای",
        "VHDL",
        "HDL",
        "Verilog",
        "FPGA",
        "میکروکنترلر",
        "میکروپروسسور",
        "ریزپردازنده",
        "Microcontroller",
        "Microprocessor",
        "Intel",
        "اینتل",
        "Apple",
        "اپل",
        "AMD",
        "Nvidia",
        "انویدیا",
        "Embedded",
        "Embedded Linux",
        "Yocto",
        "یوکتو",
        "یاکتو",
        "Electronics",
        "Robotics",
        "Mechatronics",
        "Altium",
        "Altium Designer",
        "PCB",
        "PCB Design",
        "آلتیوم",
        "آلتیوم دیزاینر",
        "Vivado",
        "Xilinx",
        "زایلینکس",
        "Altera",
        "Zynq",
        "اف پی جی ای",
        "اف‌پی‌جی‌ای",
        "کوادکوپتر",
        "کوادروتور",
        "پردازنده",
        "CPU",
        "GPU",
        "ASIC",
        "DIY",
        "سیسوگ",
        "اسنپدراگون",
        "تراشه",
        "کوالکام",
        "Qualcomm",
        "Snapdragon",
        "TSMC",
        "Chipset",
    ]

    hashtagsList = [
        "الکترونیک",
        "AppleEvent",
        "RaspberryPi",
        "آی_سی",
        "رزبری_پای",
        "رزپری_پای",
        "رسپری_پای",
        "اف_پی_جی_ای",
        "آلتیوم_دیزاینر",
        "PCBDesign",
        "AltiumDesigner",
        "EmbeddedLinux",
    ]

    mentionsList = [
        "@SimJow",
    ]

    # Add hashtags to track list with # added at the beginning of each item
    trackList = []
    for i in range(len(hashtagsList)):
        tmpStr = "#" + hashtagsList.pop()
        trackList.append(tmpStr)

    # Add keywords to track list
    trackList.extend(keywordsList)

    # create a tweepy Stream object for real time filtering of latest posted tweets
    stream = SimJowStream(
        consumer_key, consumer_secret, access_token, access_token_secret
    )
    stream.filter(track=trackList, languages=["fa"])
