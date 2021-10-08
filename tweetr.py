# Like bot for Twitter, using Python and Tweepy
# Author: Bea Lorzano
# Date: October 8, 2021
import tweepy
import random
from time import sleep
# Get keys from Twitter API
consumer_key=''
consumer_secret=''
access_token_key=''
access_token_secret=''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

f = open ("text", "r")
data = f.readlines()
api = tweepy.API(auth)
i = 0
#You can either indicate the number of times you will tweet, or just tweet once
while i<21:
    api.update_status(random.choice(data))
    print('Tweet posted successfully.')
    # Where sleep(1800), sleep is measured in seconds. 1800 sec = 30 minutes
    # Change 18000 to amount of seconds you want to have in-between tweets.
    # Read Twitter's rules on automation. Don't spam!
    sleep(1800)
    i += 1
