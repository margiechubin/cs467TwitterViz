
# coding: utf-8

# In[22]:

import csv
import json
from collections import defaultdict
from subprocess import call
import os


# In[23]:

dataJSON = defaultdict(list)

filePath = os.path.dirname(os.path.realpath(__file__)) + '/output.csv'
with open(filePath, 'r') as f:
    data = f.read().replace('\r\n', '')


# In[24]:

data = data.split('***************************************,***************************************,***************************************,***************************************')


# In[25]:

sents = []
first_line = True
hashtag = ""
for tweet_data in data:
    if (len(tweet_data) == 0):
        continue
    if (first_line == True):
        hashtag = tweet_data.split(",")[0]
        dataJSON['hashtag'] = hashtag
        first_line = False
    tweet_data = tweet_data[tweet_data.index(",")+1:]
    longitude = tweet_data[tweet_data.rfind(',')+1:]
    tweet_data = tweet_data[:tweet_data.rfind(',')]
    latitude = tweet_data[tweet_data.rfind(',')+1:]
    tweet = tweet_data[:tweet_data.rfind(',')]
    tweet = tweet.replace('\"', '')
    text = "text=%s" % (tweet)
    sents.append((os.popen("curl -d \"%s\" http://text-processing.com/api/sentiment/" % (text)).read()))
    sentiment_to_append = sents[len(sents)-1]
    if (sentiment_to_append == ''):
        dataJSON['sentiment'].append('neutral')
    else:
        dataJSON['sentiment'].append(str(json.loads(sentiment_to_append)["label"]))
    dataJSON['tweet'].append(tweet)
    dataJSON['latitude'].append(latitude)
    dataJSON['longitude'].append(longitude)


# In[26]:

with open('twitter-json.json', 'w') as outfile:
    json.dump(dataJSON, outfile)


# In[40]:




# In[ ]:



