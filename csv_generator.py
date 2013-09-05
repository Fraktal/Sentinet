#! /usr/bin/python 
  
import sys, time
import webbrowser 
import pymongo
import os
from pymongo import Connection  
from bson import BSON
from bson.json_util import dumps
from bson import Code
from bson.son import SON
import json
import cPickle as pickle
import simplejson
from operator import itemgetter
import operator, time, string
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.path as path
import numpy as np
from datetime import datetime
import random
import sys
import csv

#hashtag being tracked
hashtag_key = '#%s' %' '.join(sys.argv[1:])

COLUMNS = 1
smiley_val = {}
sad_val = {}
date_val = {}
time_val = {}
text_sad_input = {}
text_smiley_input = {}

#Mongo connection
conn = pymongo.Connection('localhost', 27017)
db = conn['neural_tweetDB']


for r in db.tweets.find(fields=["smiley", "sad", "time", "date", "tweet_text_smiley","tweet_text_sad"]):
        smiley_emoticon = smiley_val[r["smiley"]]
     	sad_emoticon = sad_val[r["sad"]]
     	date = date_val[r['date']]
     	time = time_val[r['time']]
     	text_smiley = text_smiley_input[r['tweet_text_smiley']] 
     	text_sad = text_sad_input[r['tweet_text_sad']] 



#saving time to csv file to be used in graphs outside of tweeefreak
if not os.path.isdir('data/data_csv'):
        os.makedirs('data/data_csv')

# open a file to write (mode "w"), and create a CSV writer object
csvfile = file("output.csv", "w")
csvwriter = csv.writer(csvfile)

# add headings to our CSV file
row = ["date", "time", "smiley", "sad", ]
csvwriter.writerow(row)

row = [ date, time, smiley_emoticon, sad_emoticon, text_smiley, text_sad]
csvwriter.writerow(row)

csvfile.close()