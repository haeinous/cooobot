import tweepy, time, os
from random import randint


class StreamListener(tweepy.StreamListener):
    
    """
    Class inherting from tweepy's StreamListener for @cooobot tweets
    """
    
    def on_status(self, tweet):
        """
        Called when a new status arrives.
        """
        username = tweet.user.screen_name
        text = '@' + username + ' cooo'
        tweet_id = tweet.id
        
        time.sleep(randint(1, 45))  # random time delay makes it suspenseful
        api.update_status(status=text, in_reply_to_status_id=tweet_id)


    def on_error(self, status_code):
        """
        Called when a non-200 status code is returned
        """
        if status_code == 420:
            print('Rate limited!')
            return False
        else:
            print('other error: {}'.format(status_code))
            return False


def stream(search_items):
    """
    Creates the stream listener.
    """
    stream_listener = StreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=stream_listener)
    stream.filter(track=search_items, async=True)


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(os.environ.get('consumer_key'), os.environ.get('consumer_secret'))
    auth.set_access_token(os.environ.get('access_token'), os.environ.get('access_token_secret'))
    api = tweepy.API(auth)

    try:
        stream(['@cooobot'])
    except:
        print('failure')
    finally:
        print('finally')