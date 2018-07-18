import tweepy, time, os
from random import randint

auth = tweepy.OAuthHandler(os.environ.get(consumer_key), os.environ.get(consumer_secret))
auth.set_access_token(os.environ.get(access_token), os.environ.get(access_token_secret))
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
        time.sleep(randint(1, 45))
        api.update_status(status = text, in_reply_to_status_id = tweet_id)

    def on_error(self, status_code):
        if status_code == 420:
            print('Rate limited!')

            return False

def stream(searchItems):
    streamListener = StreamListener()
    stream = tweepy.Stream(auth = api.auth, listener = streamListener)
    stream.filter(track = searchItems)


try:
    stream(['@cooobot'])
except:
    print('failure')
finally:
    print('finally')


