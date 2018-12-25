# main.py

import tweet
import follow
import time
import definitions


while True:
    
    for i in range(0, definitions.follow_people_every_cycles):
        
        # get latest rank from latest tweet
        last_rank = tweet.get_last_tweet_rank()
        print("latest rank is: {}".format(last_rank))
        
        # define new rank
        new_rank = int(last_rank)-1
        
        # define body message
        message = tweet.tweet_body(new_rank)

        #tweet
        tweet.post(message)
        
        print("Tweeted succesfully. Waiting {} secs.".format(definitions.interval_between_tweets))
        time.sleep(definitions.interval_between_tweets - (definitions.people_to_follow * definitions.interval_between_follows))

    
    # follow some people
    follow.now(definitions.people_to_follow)

