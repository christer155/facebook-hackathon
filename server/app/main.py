from flask import Flask
from flask import send_from_directory
from flask import request
from flask import jsonify
from twitter import Twitter
import os

# Flask configuration
app = Flask(__name__)
app.debug = True
app.root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'static/dist/'))
twit = Twitter() 
'''
Example usage:

	tweets = twit.get_twitter_data('iphone', 'today' or 'lastweek') - get tweets for a given keyword
	tweets = twit.traslate_tweets(twits) - replace emojis to constant words
	tweets = twit.process_tweets(twits)	- preprocessing tweets before creating the feature_vectors 
	twit.map_to_vectores(twits) - map all tweets to feature_vectores
'''

@app.route('/<path:path>', methods=['GET'])
def hello(path):
	return send_from_directory(app.root, path)

@app.route("/rate")
def rate_place():
	'''
		rate() return rating on a specific place
		example:
			/rate??place=some_value
	'''
	return jsonify(place=request.args.get('place'))

if __name__ == "__main__":
	app.run(threaded=True, port=3000)
