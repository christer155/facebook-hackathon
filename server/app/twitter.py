import re
import urllib
import urllib2
import json
import datetime
import random
import os
import pickle
from datetime import timedelta
import oauth2

class Twitter:
    #start __init__
    def __init__(self):
        self.currDate = datetime.datetime.now()
        self.weekDates = []
        self.weekDates.append(self.currDate.strftime("%Y-%m-%d"))
        self.stop_words = Twitter.get_stop_word_list(
          os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data/feature_list/stopwords.txt')))
        for i in range(1,7):
            dateDiff = timedelta(days=-i)
            newDate = self.currDate + dateDiff
            self.weekDates.append(newDate.strftime("%Y-%m-%d"))

    #start getWeeksData
    def get_twitter_data(self, keyword, time):
        self.weekTweets = {}
        if(time == 'lastweek'):
            for i in range(0,6):
                params = {'since': self.weekDates[i+1], 'until': self.weekDates[i]}
                self.weekTweets[i] = self.get_data(keyword, params)
                if len(self.weekTweets[i]) >= 50:
                  break
        elif(time == 'today'):
            for i in range(0,1):
                params = {'since': self.weekDates[i+1], 'until': self.weekDates[i]}
                self.weekTweets[i] = self.get_data(keyword, params)
            #end loop
        return self.weekTweets
    '''
        inpfile = open('data/weekTweets/weekTweets_obama_7303.txt')
        self.weekTweets = pickle.load(inpfile)
        inpfile.close()
        return self.weekTweets
    '''
    #end
    
    def parse_config(self):
      config = {}
      file_path = os.path.join(os.path.dirname(__file__), 'config.json')
      if os.path.exists(file_path):
          with open(file_path) as f:
              config.update(json.load(f))
      return config

    def oauth_req(self, url, http_method="GET", post_body=None,
                  http_headers=None):
      config = self.parse_config()
      consumer = oauth2.Consumer(key=config.get('consumer_key'), secret=config.get('consumer_secret'))
      token = oauth2.Token(key=config.get('access_token'), secret=config.get('access_token_secret'))
      client = oauth2.Client(consumer, token)
   
      resp, content = client.request(
          url,
          method=http_method,
          body=post_body or '',
          headers=http_headers
      )
      return content
    
    #start get_twitter_data
    def get_data(self, keyword, params = {}):
        maxTweets = 50
        url = 'https://api.twitter.com/1.1/search/tweets.json?'    
        data = {'q': keyword, 'lang': 'en', 'result_type': 'recent', 'count': maxTweets, 'include_entities': 0}

        if params:
            for key, value in params.iteritems():
                data[key] = value
        
        url += urllib.urlencode(data)
        
        response = self.oauth_req(url)
        jsonData = json.loads(response)
        tweets = []
        if 'errors' in jsonData:
            print "API Error"
            print jsonData['errors']
        else:
            for item in jsonData['statuses']:
                tweets.append(item['text'])            
        return tweets

    def traslate_tweets(self, tweets):
      '''
        replace emoji unicode to string representation
      '''
      if isinstance(tweets, dict):
        tweets_arr = []
        for k, v in tweets.iteritems():
          tweets_arr.extend(v)
        tweets = tweets_arr

      def happy_rep(s):
        if isinstance(s, str):
          return re.sub('(?i)\\U0001f60(?:[0-9]|[A-F])', ' happy ', str(s)).replace('\\', '')
        return s

      def sad_rep(s):
        if isinstance(s, str):
          return re.sub('(?i)\\U0001f61(?:[2-6]|E)|\
            \\U0001f62(?:[0-9]|[ABD])', ' sad ', str(s)).replace('\\', '')
        return s

      tweets = map(happy_rep, tweets)
      tweets = map(sad_rep, tweets)
      return tweets

    def process_tweets(self, tweets):
      '''
        preprocessing tweets
      '''
      def process_tweet(tweet):
        tweet = tweet.lower()
        tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
        tweet = re.sub('@[^\s]+','AT_USER',tweet)    
        tweet = re.sub('[\s]+', ' ', tweet)
        tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
        tweet = tweet.strip('\'"')
        return tweet
      return map(process_tweet, tweets)

    @staticmethod
    def get_stop_word_list(file_name):
        #read the stopwords
        stop_words = ['AT_USER', 'URL']
        fp = open(file_name, 'r')
        line = fp.readline()
        while line:
            word = line.strip()
            stop_words.append(word)
            line = fp.readline()
        fp.close()
        return stop_words

    def map_to_vectores(self, tweets):
      '''
        map list of tweets into list of vectors
      '''
      def replace_two_or_more(s):
        '''
        look for 2 or more repetitions of character
        '''
        pattern = re.compile(r"(.)\1{1,}", re.DOTALL) 
        return pattern.sub(r"\1\1", s)

      def feature_vector(tweet):
        featureVector = []  
        words = tweet.split()
        for w in words:
          #replace two or more with two occurrences 
          w = replace_two_or_more(w) 
          #strip punctuation
          w = w.strip('\'"?,.')
          #check if it consists of only words
          val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*[a-zA-Z]+[a-zA-Z0-9]*$", w)
          #ignore if it is a stopWord
          if(w in self.stop_words or val is None):
              continue
          else:
              featureVector.append(w.lower())
        return featureVector

      return map(feature_vector, tweets)

