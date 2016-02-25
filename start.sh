python twitter_tweets.py
echo "Getting Tweets..."
python twtr-parser-with-sentiment.py > /dev/null
echo "Making Visualization..."
python -m SimpleHTTPServer >/dev/null 2>&1 & #
open -a "Google Chrome" http://localhost:8000/cs467TwitterViz/map.html