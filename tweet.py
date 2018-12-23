# tweet.py

import api
import helpers
from definitions import message_hashtags, messages, my_user_id
import pandas
import medialinks
import urllib.request
import time
import tweepy
import follow

# not used
def get_image(youtube_link):
    youtube_id = youtube_link.split("=")[1]

    filename = "temp_img.jpg"

    image_url = "http://i.ytimg.com/vi/{}/hqdefault.jpg".format(youtube_id)

    urllib.request.urlretrieve(image_url, filename)

    print("image saved")

# create the tweet's body text
def tweet_body(year):
    df = pandas.read_excel("TOP-2000-2018.xlsx")

    x = year
    artist = df.artist.iloc[x]
    year = df.year.iloc[x]
    title = df.title.iloc[x]
    ranking = df.ranking.iloc[x]

    funny_text = messages[helpers.random_list_number(messages)] 

    query = artist + " " + title

    spotify_link = medialinks.get_spotify_url(query)

    youtube_link = medialinks.get_youtube_url(query)

    message = "Op plek {}, {} uit {}!\n\
--> {} - {}\n\
Luister met Spotify: {}\n\
Luister op Youtube: {}\n\
{}"\
    .format\
    (ranking, funny_text, year, 
    artist, title, 
    spotify_link, 
    youtube_link, 
    message_hashtags)

    print(message)
    
    return message
    

def post(message):
    print("...function post_tweet called")
    
    #get_image(youtube_link)
    #filename = "temp_img.jpg"
    
    # create the api
    my_api = api.make_api()
                
    # send the tweet with the image and a random message
    my_api.update_status(status=message)
    #my_api.update_with_media(filename, status=message)
    print("tweeted!")
    
def get_last_tweet_rank():
    
    my_api = api.make_api()

    # get the last tweet
    tweet = my_api.user_timeline(id = my_user_id, count = 1)[0]
    
    plek = tweet.text[8:12]
    
    return plek








