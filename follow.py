# follow.py

import tweepy
import api
import time
import definitions


# follow some people
def now(amount):

    print("...function follow called. Let's try to follow some people.")
     
    my_api = api.make_api()
     
    #Iterate through amount posts with a certain hashtag, may hit API throttling eventually
    for tweet in tweepy.Cursor(my_api.search, q = definitions.follow_hashtag, count = 10, include_entities = True).items(amount):
	    
	    userid = tweet.user.id
	    
	    if userid != definitions.my_user_id: # latter one from secrets
	    
	        try: # some users may have blocked you, so try and else continue
	    
	            my_api.create_friendship(userid)
	            print("userid {} followed".format(userid))
	            print("Waiting a bit")
	    
	            #time.sleep(definitions.interval_between_follows) #Tweet every 15 minutes
	    
	        except:
	    
	            print("Could not follow {}".format(userid))
	    
	            continue
	            
def unfollow_non_friends(amount):

    print("function unfollow_non_friends called")
    my_api = api.make_api()

    # make a list of followers
    followers = my_api.followers_ids(my_user_id)
    print("...found {} follower".format(len(followers)))
    
    # make a list if following
    following = my_api.friends_ids(my_user_id)
    print("...found {} following".format(len(following)))
       
    # makes a new list of users who don't follow you back.
    non_mutuals = list(set(following) - set(followers))
    print("...found {} non_mutuals / non_friends".format(len(non_mutuals)))
    
    # unfollow our non_friends
    if len(non_mutuals) > amount:
        for f in non_mutuals[0:amount]:
            try:
                # unfollows non follower.
                my_api.destroy_friendship(f)
                print('...Unfollowed user {}. Waiting a bit.'.format(f))
                #time.sleep(10)
            except:
                print("...could not unfollow user {}".format(f))
                continue
    else:
        print("Too few non_friends to unfollow now. Doing nothing for the moment.")
        pass

    