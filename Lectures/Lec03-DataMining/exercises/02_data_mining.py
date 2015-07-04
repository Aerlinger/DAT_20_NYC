import requests     # how python goes onto the internet!
import tweepy       # python wrapper for twitter api
import json         # javascript object notation
import time         # timey wimey stuff
import re           # regex
from BeautifulSoup import BeautifulSoup # a python HTML parser (version 3)
from bs4 import BeautifulSoup           # (version 4)

# If you're on Ubunto you may need to run `sudo apt-get install python-beautifulsoup`

## Requirements:
# BeautifulSoup4
# tweepy

# This is my own personal twitter api information
# if you could be so kind as to sign up yourself on both twitter and mashape that'd be great :)
# It's FREEEEEEE
api_key = '9SaHKiDard8rpS2ceCTthLCpA'
api_secret = 'eic5kMVRqQN7tzAnZL9QjP8LNJCdTphzhJCNka6SbdKq41LFf9'
access_token = '3092233966-0XFprtm6hBaRseggCEpOeDi7k5Q50q8gPUtU0HE'
access_secret = 'lZIMh6Vfn3Ul3xBR5OexHRjXtcOwceTl6ROEbiQZTCXBj'
mashape_key = 'ibKxXJE8bHmshlgWGIdyxEFEx7K2p12nZNRjsnGHWp4wb4APjH'



'''
Example of NO API, we will use requests and BeautifulSoup
'''

def getStockPrice(symbol): # symbol could be aapl, nflx, ge, etc
    r = requests.get('http://finance.google.com/finance?q='+symbol) # the url of the google finance page goes in here
    b = BeautifulSoup(r.text) # create a beautifulsoup object
    # b = BeautifulSoup(r.text, 'html.parser') # try this line instead if you have problems
    #print b.prettify() # will print the html nicely
    re_tag = re.compile("ref_\d+_l") #this tag finds the tag with the price in it!!!!
    span_tag = b.find('span', attrs={'id': re_tag}) 
    # use find to return THE ONE AND ONLY span tags with an id that matches our regex
    # use findAll to find all matches
    quote = span_tag.text # get the text of the tag
    return quote

print getStockPrice('aapl')


'''
Example of API but NO WRAPPER
there is no wrapper for this API, so I use requests, a python module for accessing web content
to access the information
in a sense, this is a wrapper that I just wrote for the Natural Language Processing API!
'''

def get_sentiment(phrase):
    response = requests.post("https://japerk-text-processing.p.mashape.com/sentiment/",
    headers={
        "X-Mashape-Key": mashape_key,
        "Content-Type": "application/x-www-form-urlencoded"
        },
    data={
        "language": "english",
        "text": phrase
        }
    )
    return json.loads(response.text)

# print get_sentiment("I really love this song!")



'''
Example of API WITH WRAPPER
tweepy is the python wrapper for twitter data
'''


def getTweetsOnTag(tag):
    # Documentation is your friend!

    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth) # returns a tweepy authorization handler object
    for tweet in api.search(q=tag):
        # other arguments exist, CHECK DOCUMENTATION
        # print tweet # is a BIG dictionary!!
        print tweet.created_at, tweet.text

        # http://docs.tweepy.org/en/v3.1.0/


# getTweetsOnTag("starbucks")



'''
THE BELOW CODE IS OPTIONAL
It creates a stream of a given tag!
'''

# This is the listener, resposible for receiving data
# I will not be covering this in class
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        time_ =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(decoded['timestamp_ms']) / 1000))
        handle = decoded['user']['screen_name']
        tweet_text = decoded['text'].encode('ascii', 'ignore')
        num_followers = int(decoded['user']['followers_count'])

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print '@%s at %s: %s with %d followers' % (handle, time_, tweet_text, num_followers)
        print 'sentiment: '+get_sentiment(tweet_text)['label']
        print ''
        return True
    def on_error(self, status):
        print status

def begin_live_feed(tags_to_follow):
    print "beginning live feed...."
    listener = StdOutListener()
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_secret)
    stream = tweepy.Stream(auth, listener)
    stream.filter(track=tags_to_follow)

# begin_live_feed(['@ga', '@ga_ny', '@ga_dc'])
# this is an example use, if you create a list of words and phrases, 
# a live stream of tweets about them will show up
