# api.py

import tweepy
from os import environ

try:
    import secrets 
    consumer_key = secrets.consumer_key 
    consumer_secret = secrets.consumer_secret
    access_token = secrets.access_token
    access_secret= secrets.access_secret
    
except:
    consumer_key = environ["consumer_key"]
    consumer_secret = environ["consumer_secret"]
    access_token = environ["access_token"]
    access_secret = environ["access_secret"]

#create an OAuthHandler instance. Twitter requires all requests to use OAuth for authentication
def make_api():

    print("...function make_api called")
    
    try:
    
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

        # set the access tokens
        auth.set_access_token(access_token, access_secret)
    
        #Construct the API instance
        api = tweepy.API(auth)
        print("...api created")
        
        return api
            
    except:
        print("...unable to create api")
        