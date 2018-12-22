# definitions.py

# search query to find pictures. No AND operator or similar needed.
search_query = [
"cute",
"feline"
]

# twitter user id
my_user_id = 1075733110455762944

# follow people tweeting with this hashtag
follow_hashtag = "#top2000"

# hashtags to be added in each tweet
message_hashtags = "#top2000 #top2000twitstream"

# define the message
messages = [
"deze super hit",
"dit prachtige nummmer",
"deze fantastische plaat",
"dit onvergetelijke nummer",
"deze topplaat",
"dit monument uit de muziekgeschiedenis",
"dit hoogtepunt uit de popmuziek",
"deze plaat die iedereen kent",
"deze jeugdherinnering",
"deze tijdloze single",
"deze single die iedereen kent",
"dit nummer dat iedereen mee kan zingen",
"deze gouwe ouwe",
"deze topper",
"deze hit die het altijd goed doet",
"deze onvergetelijke plaat",
"deze knaller",
"deze gave plaat",
"onze persoonlijke favoriet",
"deze tophit",
"onze lievelingsplaat"
]

 

# DO NOT EDIT THIS SECTION

#join the query words, separated by %20
base_url = "https://pixabay.com/en/photos/{}/?image_type=photo&pagi=".format("%20".join(search_query))  