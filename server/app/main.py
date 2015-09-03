from flask import Flask
from flask import jsonify
from twitter import Twitter

app = Flask(__name__)
twit = Twitter() # example: tweets = twit.getTwitterData('iphone', 'today' or 'lastweek')

@app.route("/")
def hello():
	return jsonify(foo="bar")

if __name__ == "__main__":
	app.run(threaded=True, port=3000)