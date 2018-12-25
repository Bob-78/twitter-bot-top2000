# main.py

import tweet
import follow
import time
from definitions import interval_between_tweets


while True:
    
    for i in range(0, 3):
        
        #try:
        # get latest rank from latest tweet
        last_rank = tweet.get_last_tweet_rank()
        print("latest rank is: {}".format(last_rank))
        
        # define new rank
        new_rank = int(last_rank)-1
        
        # define body message
        message = tweet.tweet_body(new_rank)

        #tweet
        tweet.post(message)
        
        print("Tweeted succesfully. Waiting {} secs.".format(interval_between_tweets))
        time.sleep(interval_between_tweets)
    
        #except:
        #    print("Could not tweet. Waiting 300 secs.")
        #    time.sleep(300)
        #    pass
    
    # follow some people
    follow.now(1)

