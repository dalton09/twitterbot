import tweepy
from time import sleep
import sys
from tweepy import Stream
from tweepy.streaming import StreamListener

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

# Get tweets tweeted or rt'd by @boltiot
bolt = api.user_timeline(screen_name = 'boltiot', count = 100, include_rts = True)

bolt2 = api.get_user(screen_name = '@TestBoltIot')

handle = bolt2.id;
print (handle)


'''
user = []
handle = 'boltiot'
user.append(handle)
'''
























public_tweets = api.home_timeline()
#for tweet in public_tweets:
    #print (tweet.text)
    #print ("----------------------")

print ('\nAccount Username : ' + myBot.screen_name)
print ('\nNumber of followers : ' + str(myBot.followers_count))
print('******************************\n LIST OF FOLLOWERS\n******************************\n')

for follower in myBot.followers():
    try:
        print (follower.screen_name)
    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

print('\n******************************\n')

print('\n\n******************************\n FOLLOWING \n******************************\n')








for friend in myBot.friends():
    try:
       print (friend.screen_name)
    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break

print('\n******************************\n')









class listener(StreamListener):

    def on_status(self, status):

        print (status.text)


    def on_error(self, status_code):
        #print (sys.stderr)
        print ('Encountered error with status code:')
        print (status_code)
        return True # Don't kill the stream

    def on_timeout(self):
        #print  (sys.stderr)
        print ('Timeout...')
        return True # Don't kill the stream

# Create a streaming API and set a timeout value of ??? seconds.

streaming_api = Stream(auth, listener(), timeout=None)

# Optionally filter the statuses you want to track by providing a list
# of users to "follow". follow=['458269836'],

streaming_api.filter(follow=['902092143455379456'])



















'''


for bolt_tweets in bolt:
    try:
        print(bolt_tweets.text)
        print('-----------------')
    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break



# For loop to iterate over tweets with #IOT, limit to 20

for tweet in tweepy.Cursor(api.search,q='#IOT').items(20):

# Print out usernames of the last 20 people to use #IOT

    try:
        print (tweet.text)
        print('Tweet by: @' + tweet.user.screen_name)
        
        # Favorite the tweet
               
        tweet.favorite()
        print('Favorited the tweet')
        print('-----------------')
        sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
'''
