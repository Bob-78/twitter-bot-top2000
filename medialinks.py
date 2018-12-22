# medialinks.py

import helpers

def get_youtube_url(query):
    try:
        print("function get_youtube_url called")
        query = query.replace("&", "") # else the google search goes wrong for womack & womack etc.
        query = query.replace(" ", "+") + "+youtube"
    
        search_url = "https://www.google.com/search?q={}".format(query)
    
        print("search url used: {}".format(search_url))
    
        soup = helpers.get_soup(search_url)
    
        # get the first watch link and clean it up
        link = str(soup.select_one("a[href*=youtube.com/watch]")) # convert into string for manipulation
        link = link.split("q=")[1] # remove prefix
        link = link.split("&")[0] # remove suffix
        link = link.replace("%3Fv%3D", "?v=")
    
        print("returning youtube link: {}".format(link))
        return(link)

    except:
        return("Could not get Youtube URL")
    
def get_spotify_url(query):
    try:
        print("function get_spotify_url called")
    
        query = query.replace("&", "") # else the google search goes wrong for womack & womack etc.
        query = query.replace(" ", "+") + "+spotify"
    
        search_url = "https://www.google.com/search?q={}".format(query)
    
        print("search url used: {}".format(search_url))
    
        soup = helpers.get_soup(search_url)
    
        # get the first watch link and clean it up
        link = str(soup.select_one("a[href*=open.spotify]")) # convert into string for manipulation
        link = link.split("q=")[1] # remove prefix
        link = link.split("&")[0] # remove suffix

        print("returning spotify link: {}".format(link))
        return(link)

    except:
        return("Could not get Spotify URL")