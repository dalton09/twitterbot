import tweepy
from time import sleep

consumer_key='avjJFVLqGLp4JCW6e3DC6I8Te'
consumer_secret='UcNJKyHVGOkMJimP6t1eaocqow0PVDIpp3Ko0MBaidZXTkAcEg'
access_token='902064299597692929-uXOc9SciXw0EGZLDAt5otVibwHfX4bg'
access_token_secret='7L1zYV8FZ8zI7eAx0AMIFrtxmlePYmxHUQr4CzrjX4SsY'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
auth.secure = True
api = tweepy.API(auth)

# Get the User object for twitter...
myBot = api.get_user(screen_name = '@DaltonBoltTest')


public_tweets = api.home_timeline()
#for tweet in public_tweets:
    #print (tweet.text)
    #print ("----------------------")

print (myBot.screen_name)
print (myBot.followers_count)

for friend in myBot.friends():
   print (friend.screen_name)

# For loop to iterate over tweets with #IOT, limit to 40
for tweet in tweepy.Cursor(api.search,q='#IOT').items(40):

# Print out usernames of the last 40 people to use #IOT

    try:
        print (tweet.text)
        print('Tweet by: @' + tweet.user.screen_name)
        print('-----------------')

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
