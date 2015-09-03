from flask import Flask
from flask import jsonify
from twitter import Twitter

app = Flask(__name__)
twit = Twitter() 
'''
Example usage:

	tweets = twit.get_twitter_data('iphone', 'today' or 'lastweek') - get tweets for a given keyword
	tweets = twit.traslate_tweets(twits) - replace emojis to constant words
	tweets = twit.process_tweets(twits)	- preprocessing tweets before creating the feature_vectors 
	twit.map_to_vectores(twits) - map all tweets to feature_vectores
'''
@app.route("/")
def hello():
	return jsonify(foo="bar")

if __name__ == "__main__":
	app.run(threaded=True, port=3000)