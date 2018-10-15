#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


#Variables that contains the user credentials to access Twitter API
access_token = ""#Enter your access token
access_token_secret = ""#Enter your access token secret
consumer_key = "" #Enter your consumer key
consumer_secret = ""#Enter your consumer key secret

class TwitterStreamer():

    def stream_tweets(self,fetched_tweets_filename,hash_tag_list):
        l = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        stream = Stream(auth, l)
        stream.filter(track=hash_tag_list)


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def _init_(self, fetched_tweets_filename) :
        self.fetched_tweets_filename = fetched_tweets_filename

    def on_data(self, data):
        try :
            print (data)
            with open(self.fetched_tweets_filename,'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data: %s" %str(e))
            return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    hash_tag_list =["Malaysia"]
    fetched_tweets_filename = "tweets.txt"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename,hash_tag_list)
