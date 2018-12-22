# Twitter-bot-Top2000

This is a Python Twitter bot for deployment on Heroku

With regular intervals, it posts links to Top2000 songs

To get it up and running on Heroku
1. Install Heroku
2. Open a terminal in the app folder
3. git init
4. heroku create app-name
5. git add . 
6. git commit -m "commitmessage"
7. git push heroku master
8. set the environment variables: (replace "secret" with your codes from https://developer.twitter.com)

- heroku config:set access_secret=secret
- heroku config:set access_token=secret
- heroku config:set consumer_key=secret
- heroku config:set consumer_secret=secret

9. heroku ps:scale worker=1

Procfile (no extension) should contain the following line:
worker: python main.py

requirements.txt should contain the list of modules needed for the app to run
You can generate the file with:
1. pip freeze > requirements.txt.

Push to github: #CHANGE
1. git push https://github.com/Bob-78/Twitter-bot-cats.git master

