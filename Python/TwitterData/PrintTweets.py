import tweepy
import csv
from textblob import TextBlob
from TwitterData import resources

consumer_key=resources.consumer_key
consumer_secret=resources.consumer_secret
access_token=resources.access_token
access_token_secret=resources.access_token_secret
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)
topic='India'
tweets=[]
s_polarity=[]
s_subjectivity=[]
public_tweets = api.search(topic)

for tweet in public_tweets:
    tweets.append(tweet.text)
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    s_polarity.append(analysis.sentiment[0])
    s_subjectivity.append(analysis.sentiment[1])
    print(analysis.sentiment)

with open('Tweets.csv','w',newline='') as csvfile:
    fieldnames=['Topic','Tweet','Sentiment Polarity','Sentiment Subjectivity'] 
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(tweets)):
        writer.writerow({'Topic': topic, 'Tweet': tweets[i], 'Sentiment Polarity':s_polarity[i],'Sentiment Subjectivity':s_subjectivity[i]})
