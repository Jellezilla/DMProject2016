import json
from twitter import Twitter, OAuth, TwitterHTTPError
import tweepy
from tweepy import OAuthHandler
import os 
import random


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


t = Twitter(
    auth=OAuth(access_token, access_secret, consumer_key, consumer_secret))


def search_tweets(q, count = 100, result_type = "recent"):
	"""
		Returns a list of tweets matching a certain phrase (hashtag, word, etc.)
	"""

	return t.search.tweets(q=q, result_type=result_type, count=count)



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

	i = 2
	
	result = t.search.tweets(q=keywords, count=10, result_type="popular", lang="en")
	

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

GetTweetList()

