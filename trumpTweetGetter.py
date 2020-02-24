import tweepy

from dotenv import load_dotenv
load_dotenv()
import os
consumer_key = os.getenv("APIkey")
consumer_secret = os.getenv("APIsecret")
access_token = os.getenv("accessToken")
access_token_secret = os.getenv("accessTokenSecret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('realDonaldTrump')
print(user.screen_name)

curTweets = api.user_timeline(screen_name = user.screen_name, count = 200, tweet_mode='extended')
oldest = curTweets[-1].id - 1
allTweetsFullText = []

for x in curTweets:
    allTweetsFullText.append(x.full_text)

while (len(allTweetsFullText) < 1000):
    curTweets = api.user_timeline(screen_name = user.screen_name, count = 200, tweet_mode='extended', max_id=oldest)
    oldest = curTweets[-1].id - 1

    for x in curTweets:
        allTweetsFullText.append(x.full_text)
    

print(len(allTweetsFullText))

f = open("tweets.txt", "w")
curCount = 1
for x in allTweetsFullText:
    if x.split()[0] != "RT":
        f.write("tweet: " + x + "\n")
    curCount += 1