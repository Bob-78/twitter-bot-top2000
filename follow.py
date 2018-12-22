# follow.py

import tweepy
import api
import time
from definitions import my_user_id, follow_hashtag


# follow some people
def now(amount):

    print("...function follow called. Let's try to follow some people.")
     
    my_api = api.make_api()
     
    #Iterate through amount posts with a certain hashtag, may hit API throttling eventually
    for tweet in tweepy.Cursor(my_api.search, q = follow_hashtag, count = 10, include_entities = True).items(amount):
	    
	    userid = tweet.user.id
	    
	    if userid != my_user_id: # latter one from secrets
	    
	        try: # some users may have blocked you, so try and else continue
	    
	            my_api.create_friendship(userid)
	            print("userid {} followed".format(userid))
	            print("Waiting a bit")
	    
	            time.sleep(10) #Tweet every 15 minutes
	    
	        except:
	    
	            print("Could not follow {}".format(userid))
	    
	            continue
	            