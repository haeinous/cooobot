import tweepy
import random
import time
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


class StreamListener(tweepy.StreamListener):
  def on_status(self, tweet):

    #retweets of tweets containing @cooobot are ignored
    if tweet.retweeted_status:
      return

    #print(tweet)
    username = tweet.user.screen_name
    text = '@' + username + ' cooo'
    tweet_id = tweet.id
    
    #random time delay makes it suspenseful
    time.sleep(random.randint(1,45))
    api.update_status(status = text, in_reply_to_status_id = tweet_id)

  def on_error(self, status_code):
    if status_code == 420:
       print('Rate limited!')

       return False

def stream(searchItems):
  streamListener = StreamListener()
  stream = tweepy.Stream(auth = api.auth, listener = streamListener)
  stream.filter(track=searchItems)


try:
  stream(['@cooobot'])
except:
  print("Failure")

def add(x, y):
  return x + y

z = add(2, 3)

def add_only_positive_integers(x, y):
  if x < 0 or y < 0:
     return
     dfdf
  else:
    return x + y


def print_coo():
  print("coo")
  return


