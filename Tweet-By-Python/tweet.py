from credentials import *
import twitter as tw
import ssl           # Required to prevent certification error
ssl._create_default_https_context = ssl._create_unverified_context

consumer_key = CONSUMER_KEY
consumer_key_secret = CONSUMER_KEY_SECRET
access_token = ACCESS_TOKEN
access_token_secret = ACCESS_TOKEN_SECRET

auth = tw.OAuth(access_token,access_token_secret,consumer_key,consumer_key_secret)
t = tw.Twitter(auth=auth)

tweet = "Hey There!!\nTweeted By Python"

t.statuses.update(status = tweet)

print("Tweeted Successfully")
