# main.py

import tweet
import follow
import time
from definitions import base_url


while True:
    
    for i in range(0, 4):
        
        try:
            last_rank = tweet.get_last_tweet_rank()
            print("latest rank is: {}".format(last_rank))
            new_rank = int(last_rank) -1

            message = tweet.tweet_body(new_rank)
    
            tweet.post(message)
            
            print("Tweeted succesfully. Waiting 300 secs.")
            time.sleep(300)
    
        except:
            print("Could not tweet. Waiting 300 secs.")
            time.sleep(300)
            pass
    
    follow.now(1)
