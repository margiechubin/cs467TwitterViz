
# coding: utf-8

# In[1]:

from twitter import *

import sys
import csv


# In[3]:

unique_rows = []

# akshat's info
CONSUMER_KEY = '4QozbzGJsTzvqZaJiDIbjwH41'
CONSUMER_SECRET = 'IMri9pQWd3dHCLl2hXDdh85sA8Xs9sVC1B6Hx6q232vTnWcTZq'
OAUTH_TOKEN = '3085949459-5NLUoC1KrTdhvsW7W7N8budB8bFsbVKzFiXuxay'
OAUTH_TOKEN_SECRET = 'j0nex8Mewv0tAznYlKVRsTZJ1SuBmdm3oLD13bjILa7uf'

# surtai's info
#CONSUMER_KEY = 'JiuMK80bhNNPXog8i20jaNah4'
#CONSUMER_SECRET = 'wOHJXY6Szjn5l7jsndsIeM6mtOPh4nGzAXkituknh0zWGRrnYS'
#OAUTH_TOKEN = '97078590-znIQVH7XK5f8VpdWKhgTdD96W1RFBSlJzPz0Lr9xI'
#OAUTH_TOKEN_SECRET = 'Tv75DmZmes1S3PMtBYtncZUUCH8MGJsLTCIZpRgEn8WEQ'

# In[9]:

latitude = 34.5133 # geographical centre of search
longitude = -94.1629 # geographical centre of search
max_range = 6371.393     # search range in kilometres
num_results = 100 # minimum results to obtain
outfile = "output.csv"
csvfile = file(outfile, "w")
csvwriter = csv.writer(csvfile)


# In[5]:

twitter = Twitter(auth = OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))


# In[10]:

result_count = 0
last_id = None
q = raw_input("Enter hashtag\n")
row = [ q, q, q, q ]
csvwriter.writerow(row)
while result_count <  num_results:
    # the maximum count allowed here is 100
    query = twitter.search.tweets(q = q, geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)
    for result in query["statuses"]:
        if result["geo"]:
            user = result["user"]["screen_name"]
            text = result["text"]
            text = text.encode('ascii', 'replace')
            latitude = result["geo"]["coordinates"][0]
            longitude = result["geo"]["coordinates"][1]

            # now write this row to our CSV file
            row = [ user, text, latitude, longitude ]
            if (row not in unique_rows):
                csvwriter.writerow(row)
                unique_rows.append(row)
                stars = "***************************************"
                new_row = [stars, stars, stars, stars]
                csvwriter.writerow(new_row)
                result_count += 1
            else:
                sys.exit(1)
            last_id = result["id"]
    # print "got %d results total so far" % result_count

csvfile.close()
print "written to %s" % outfile


# In[ ]:
