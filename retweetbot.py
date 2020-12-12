import tweepy
import time
import random
import os
from userids import user_ids


# Authenticate to Twitter
auth = tweepy.OAuthHandler("ConYb1zQ7WhBEYPfxVsi1zt0w",
                           "g4ujAFUq0TZtSDogGfj7p1i4kxmSPoTvL6BYGfHLclFRWRVhnh")
auth.set_access_token("956507305960509440-WyKQ83Kac4w4WOqiZQylndVgwAD1wc2",
                      "6gi3toMbAyYTMDWkmdaGjr93n5nlwKvhfhkDmFYvPv09t")


api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)


for tweet in tweepy.Cursor(api.user_timeline, id=random.choice(user_ids)).items(4):
    try:
        tweet.retweet()
    except StopIteration:
        break
