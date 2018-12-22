# helpers.py

import requests
from bs4 import BeautifulSoup
from random import randint


# helper function to get soup form a url
def get_soup(soup_url):        
    print("...function get_soup called")

    # requesting the html
    response = requests.get(soup_url)

    # parse the html using beautiful soup and store in variable
    soup = BeautifulSoup(response.text,"html.parser")  
    
    print("returning soup")

    return soup

        
# helper function to get a random list number
def random_list_number(list_name):    
    print("...function random_list_number called") 
    
    random_list_number = randint(0, len(list_name)-1)
    
    return random_list_number 
    
# removes all tweets without warning...
def delete_all_tweets():
    my_api = api.make_api()

    for status in tweepy.Cursor(my_api.user_timeline).items():
        try:
            my_api.destroy_status(status.id)
            print("Deleted: {}".format(status.id))
        except:
            print("Failed to delete: {}".format(status.id))
                
    