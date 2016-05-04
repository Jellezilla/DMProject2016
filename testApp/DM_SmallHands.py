import json
from twitter import Twitter, OAuth, TwitterHTTPError
import tweepy
from tweepy import OAuthHandler
import os 
import random
import unicodecsv as csv
import unicodedata


#token = "719079938364743680-fAPWjBr51T13EYki1N8ubuobiX7j6Ni"
#token_secret = "dQS3F5aoXNnTpbJL3ISeeQAh0cO6CiaYG1BnI2OWypUtw"

#con_secret = "k4A1jajBxtQYYJbITHigAYjdG"
#con_secret_key = "	kEmovRpDKZ3Pde3xLdc8qPNGVBUZnxMX0GNwQYOmCHvREII1JK"

TWITTER_HANDLE = "SmallHandsHunter"

consumer_key = 'k4A1jajBxtQYYJbITHigAYjdG'
consumer_secret = 'kEmovRpDKZ3Pde3xLdc8qPNGVBUZnxMX0GNwQYOmCHvREII1JK'
access_token = '719079938364743680-fAPWjBr51T13EYki1N8ubuobiX7j6Ni'
access_secret = 'dQS3F5aoXNnTpbJL3ISeeQAh0cO6CiaYG1BnI2OWypUtw'

#auth = OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_secret)
 
#api = tweepy.API(auth)



already_tweeted_id = []

DATA_SET = "data-set2.csv"
#DATA_SET = "data-set.csv"

t = Twitter(
    auth=OAuth(access_token, access_secret, consumer_key, consumer_secret))


def search_tweets(q, count = 100, result_type = "recent"):
	"""
		Returns a list of tweets matching a certain phrase (hashtag, word, etc.)
	"""

	return t.search.tweets(q=q, result_type=result_type, count=count)

def WriteTweetToFile(count = 50, result_type = "popular"):

	naughty_words = []
	#good_words = ["trump", "donald", "bernie", "sanders", "president", "campaign", "election", "small hands"]
	good_words = ["trump", "donald", "MakeAmericaGreatAgain", "bernie", "sanders", "election", "hillary", "clinton", "vote", "cruz", "choosecruz", "crooked", "donaldtrump", "hillaryclinton"]
	filter = " OR ".join(good_words)
	blacklist = " -".join(naughty_words)

	keywords = filter + blacklist


	result = t.search.tweets(q=keywords, count=count, result_type="recent", lang="en")
	
	i = random.randint(0,count)

	#print count
	#header = [['User', 'User id', 'User description', 'location', 'time zone', 'user language', 'followers count', 'user follows count', 'tweet count', 'profile created', 'default profile img', 'user verified',
	#					'tweet text', 'tweet id', 'tweeted at', 'favorite count','retweeted','retweet count','language','geo','hashtags','urls', 'friends']]


	#with open(DATA_SET, 'wb') as out_file:
	#	writer = csv.writer(out_file, delimiter=',')
	#	writer.writerows(header)
		
		
	
	#while(i < count):
	try:
		if not result["statuses"][i]["id"] in already_tweeted_id:
			data = []

			data.append(result["statuses"][i]["user"]["name"])
			data.append(result["statuses"][i]["user"]["id"])
			data.append(result["statuses"][i]["user"]["description"])
			data.append(result["statuses"][i]["user"]["location"])
			data.append(result["statuses"][i]["user"]["time_zone"])
			data.append(result["statuses"][i]["user"]["lang"])
			data.append(result["statuses"][i]["user"]["followers_count"])
			data.append(result["statuses"][i]["user"]["friends_count"])
			data.append(result["statuses"][i]["user"]["statuses_count"])
			data.append(result["statuses"][i]["user"]["created_at"])
			data.append(result["statuses"][i]["user"]["default_profile_image"])
			data.append(result["statuses"][i]["user"]["verified"])
			data.append(result["statuses"][i]["text"])
			data.append(result["statuses"][i]["id"])
			data.append(result["statuses"][i]["created_at"])
			data.append(result["statuses"][i]["favorite_count"])
			data.append(result["statuses"][i]["retweeted"])
			data.append(result["statuses"][i]["retweet_count"])
			data.append(result["statuses"][i]["lang"])
			data.append(result["statuses"][i]["geo"])
			data.append(result["statuses"][i]["entities"]["hashtags"])
			data.append(result["statuses"][i]["entities"]["urls"])

			data.append(GetFriendsList(result["statuses"][i]["user"]["id"]))
			
			
#				i += 1


			AddTweetToDataSet(data)
		#writer.writerow(data)
	except IndexError: 
		None
	finally: 
		#i += 1
		None
def WriteHeaderToNewFile():
	header = [['User', 'User id', 'User description', 'location', 'time zone', 'user language', 'followers count', 'user follows count', 'tweet count', 'profile created', 'default profile img', 'user verified',
						'tweet text', 'tweet id', 'tweeted at', 'favorite count','retweeted','retweet count','language','geo','hashtags','urls', 'friends']]


	with open(DATA_SET, 'wb') as out_file:
		writer = csv.writer(out_file, delimiter=',')
		writer.writerows(header)
		
		



def GetFriendsList(_userID):
	friendlist = []
	query=t.friends.ids(user_id=_userID)
	for n in range(0, len(query["ids"]), 100):
		ids = query["ids"][n:n+100]
		subquery = t.users.lookup(user_id = ids)
		for user in subquery:
			friendlist.append(user["screen_name"])
	print len(friendlist)
	return friendlist


def WriteFriendsToDataSet():
	with open (DATA_SET, 'rb') as in_file:
		reader = csv.reader(in_file, delimiter=',')
		headerRow = reader.next()
		headerRow.append('Friends')
		print(headerRow)

		with open(DATA_SET, 'ab') as out_file:
			writer = csv.writer(out_file, delimiter=',')
			writer.writerow(headerRow)

		

def AddTweetToDataSet(data):
	with open(DATA_SET, 'ab') as out_file:
		writer = csv.writer(out_file, delimiter=',')
		
		writer.writerow(data)




def UpdateTweetList():
	with open(DATA_SET, 'rb') as out_file:
		reader = csv.reader(out_file, delimiter=',')
		for column in reader:
			try:
				#print column[13]
				already_tweeted_id.append(column[13])
			except IndexError:
				print "index out of range biatch!" 
	#print(already_tweeted_id)
	print(str(len(already_tweeted_id))+" lines of data in csv file")

# old method
def GetTweetList():
	# A list of bad words to search for. Words found on list are mainly gathered from the words in spam tweets.  
	#naughty_words = ["-pussy", "penis", "sex", "teen", "teens", "hardcore", "ass", "porn", "cock", "anal", "sexy", "boobs", "tits", "suck", "lesbian", "lesbians", "horny", "vote", "album", "NFL", "download"]
	# A list of good words to search for that fits the fictive characters persona. 
	good_words = ["trump", "donald", "bernie", "sanders", "president", "campaign", "election", "small hands"]
	#OR is Twitter's search operator to search for this OR that
	filter = " OR ".join(good_words)

	# The - is Twitter's search operator for negative keywords
	#blacklist = " -".join(naughty_words)

	#This will search for any words in good_words minus any naughty_words
	#keywords = filter + blacklist
	keywords = filter

	
	i = 1
	result = t.search.tweets(q=keywords, count=10, result_type="popular", lang="en")
	
	#q=keywords
	#result = t.search.tweets(q, count, result_type, lang)

	print "*** User info: ***"
	print "Tweet by user: ", 		result["statuses"][i]["user"]["name"] 
	print "User id: ",				result["statuses"][i]["user"]["id"]
	print "User description: ", 	result["statuses"][i]["user"]["description"]
	print "Location: ",				result["statuses"][i]["user"]["location"]
	print "time zone: ",			result["statuses"][i]["user"]["time_zone"]
	print "user language: ",		result["statuses"][i]["user"]["lang"]
	print "followers_count: ", 		result["statuses"][i]["user"]["followers_count"]
	print "user follows count: ", 	result["statuses"][i]["user"]["friends_count"]
	print "tweet count: ",			result["statuses"][i]["user"]["statuses_count"]
	print "profile created: ", 		result["statuses"][i]["user"]["created_at"]
	print "default profile img: ",  result["statuses"][i]["user"]["default_profile_image"]
	print "user verified: ", 		result["statuses"][i]["user"]["verified"]
	print ""

	print "*** Tweet info: ***"
	print "Tweet: ", 		 		result["statuses"][i]["text"]
	print "Tweet id: ",				result["statuses"][i]["id"]
	print "Time tweeted: ",			result["statuses"][i]["created_at"]
	print "favorite_count: ",   	result["statuses"][i]["favorite_count"]
	print "Is retweet: ", 			result["statuses"][i]["retweeted"]
	print "retweet_count: ", 		result["statuses"][i]["retweet_count"]
	print "Language: ", 			result["statuses"][i]["lang"]
	print "Geo: ",					result["statuses"][i]["geo"]	
	print ""	

	print "*** Tweet Entities: ***"
	print "Hashtags: ",				result["statuses"][i]["entities"]["hashtags"]
	print "Urls: ",					result["statuses"][i]["entities"]["urls"]
	print ""



#GetTweetList()

# updates the 
#UpdateTweetList()

# seraches for tweets based on parameters found in the method and writes them to the csv file
WriteTweetToFile()
#FindUserFriends()
#WriteFriendsToDataSet()
#WriteHeaderToNewFile()