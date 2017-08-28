#Creator - Dalton De Souza
import tweepy
from time import sleep
import sys
from tweepy import Stream
from tweepy.streaming import StreamListener


#authentication and api keys
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
bolt = api.get_user(screen_name = '@boltiot')
handle = bolt.id;
public_tweets = api.home_timeline()

#printing the details of the account

print ('\nAccount Username : ' + myBot.screen_name)
print ('\nNumber of followers : ' + str(myBot.followers_count))
print('******************************\n LIST OF FOLLOWERS\n******************************\n')

#printing the followers of the account
for follower in myBot.followers():
    try:
        print (follower.screen_name)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
print('\n******************************\n')
print('\n\n******************************\n FOLLOWING \n******************************\n')


#printing thw list of profiles followed by the account
for friend in myBot.friends():
    try:
       print (friend.screen_name)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
print('\n******************************\n')


# For loop to iterate over tweets with #IoT, limit to 40
print('\n******************************')
print('\n fetching 40 tweets with #IoT and liking them if not done already')
print('\n******************************\n')


# Print out usernames of the last 40 people to use #IOT
for tweet in tweepy.Cursor(api.search,q='#IoT').items(40):      #q='search query', .items(40) - 40 tweets
    try:
        print (tweet.text)
        print('Tweet by: @' + tweet.user.screen_name)
        
        # Favorite the tweet
        
        tweet.favorite()
        print('Favorited the tweet')
        print('--------------------------')
        sleep(6)
    except tweepy.TweepError as e:
        print(e.reason)
        print('--------------------------')
    except StopIteration:
        break


#This class is a listener that monitors @boltiot's twitter feed for new tweets and favourite's them
class listener(StreamListener):
    def on_status(self, status):
        print ("\n\n************************************\n TWEETED BY @boltiot\n************************************\n")
        print (status.text)
        id = status.id
        try:
            api.create_favorite(id)
            print('\n\nLiked this tweet')
            print("************************************\n")
        except tweepy.TweepError as e:
            print(e.reason)
            return True         # Don't kill the stream

    def on_error(self, status_code):
        print ('Encountered error with status code:')
        print (status_code)
        return True             # Don't kill the stream

    def on_timeout(self):
        print ('Timeout...')
        return True             # Don't kill the stream

# Create a streaming API and no timeout.
streaming_api = Stream(auth, listener(), timeout=None)

# filter the statuses you want to track by providing a list, this filter contains the Account Id
# of @boltiot

streaming_api.filter(follow=['458269836'])



# Twitter Account ID of working test account
#Creator - Dalton De Souza
# streaming_api.filter(follow=['902092143455379456'])
