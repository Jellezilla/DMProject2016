import csv
from collections import defaultdict

#columns = defaultdict(list) # each value in each column is appended to a list
DATA_SET = "data-set.csv"
DESIRED_COLUMNS = ('User', 'User id', 'User description', 'location', 'time zone', 'user language', 'followers count', 'user follows count', 'tweet count', 'profile created', 'default profile img', 'user verified',
						'tweet text', 'tweet id', 'tweeted at', 'favorite count','retweeted','retweet count','language','geo','hashtags','urls')

already_tweeted_id = []

i=0
with open(DATA_SET, 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for column in reader:
        try:
#	        print column[13]
        	already_tweeted_id.append(column[13])
        except(IndexError):
        	print "index out of range biatch!" 

print already_tweeted_id


