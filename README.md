# cs467 Twitter Visualization
This is the visualization my group created for a group project in CS 467.
### To see a snapshot of the visualization:
go to http://margiechubin.github.io/cs467TwitterViz/

### To run the script:
* download all the files
* run these commands in a bash shell
  * pip install twitter 
  * sudo chmod 777 start.sh
  * ./start.sh 
* When prompted for a hashtag, type the hashtag you want to search for without the hashtag symbol itself. If a browser window doesn't automatically open up after the results are fetched and parsed, then manually open up a browser and go to "localhost:8000" (without the quotes). A webpage will be hosted there.

### Important files included are:
* start.sh: install script to bind the backend and front end
* twitter-tweets.py: get tweets based on hashtag from Twitter API
* twtr-parser-with-sentiment.py: run sentiment analysis on tweets
* index.html: the front end visualization
* various json files: user can see a few selected hashtag visualizations on the website
