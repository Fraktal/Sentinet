#! /usr/bin/python

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream 
import sys
import credentials
import simplejson as json 
<<<<<<< HEAD
import jsonpickle  
=======
import jsonpickle
import re 

#credentials for Twitter OAuth 
CONSUMER_KEY = credentials.CONSUMER_KEY
CONSUMER_SECRET = credentials.CONSUMER_SECRET
ACCESS_TOKEN = credentials.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = credentials.ACCESS_TOKEN_SECRET


class StdOutListener(StreamListener):
  
    #tweets and Mongo
    def on_status(self, status):  

         #simplified and readable date for the tweets
         date = status.created_at.date().strftime("20%y/%m/%d")  
         time = status.created_at.time().strftime("%H:%M:%S")#GMT time 

         #send data to file for analysis
         print jsonpickle.encode(status)


    #error handling
    def on_error(self, error):
        print error 

    
     
if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET )
    print >> sys.stderr,"retrieving data......"
    stream = Stream(auth, listener)    
    stream.filter(track=[':)', ':('])