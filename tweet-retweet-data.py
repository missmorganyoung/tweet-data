import json

tweetFile = open("./tweets_small.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()

print(tweetData[2]["lang"])

sum = 0
total_tweets = 0

for tweet in tweetData:
    if "user " and "followers_count" in tweet["user"]:
        sum = sum + tweet["user"]["followers_count"]
        total_tweets = total_tweets + 1

average_retweet = sum / total_tweets

print(average_retweet)
