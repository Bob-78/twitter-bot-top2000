# api.py

import tweepy
from os import environ

consumer_key="nw3Zb4zhJVSzNSTGrcgMnqaZo"
consumer_secret="tKuIj1KLVpb3fkswSsmKG6zVPuF837ZAr3FOcFhKoexOvai1fb"
access_token="1075733110455762944-E7R71Oi4HAy5mXKq21aBda016mtoYK"
access_secret="VMllwhRRij3ePLmjqQjGZYeIEJEj0MUkbCh0YbecC50A8"

#consumer_key = environ["consumer_key"]
#consumer_secret = environ["consumer_secret"]
#access_token = environ["access_token"]
#access_secret = environ["access_secret"]

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
        