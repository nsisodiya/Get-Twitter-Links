#!/usr/bin/python
#By -  Narendra Sisodiya - http://narendrasisodiya.com

from GetTwitterLib import *

## http://www.untiny.me/api/1.0/extract/?url=aHR0cDovL3Rpbnl1cmwuY29tL2Nmb2VwOA==&format=text&enc=64
## http://untiny.me/api/1.0/extract?url=http://tiny.pl/htk&format=text 
## print urlopen("http://api.twitter.com/1/statuses/user_timeline.xml?include_entities=false&include_rts=true&screen_name=nsisodiya&count=1").read()
## #TODO -- http://eubolist.wordpress.com/2010/12/24/python-script-merge-and-sort-multiple-rss-feed-items-in-one-feed/



print "Welcome to Linux Links"


file_listuser=open('listuser', 'r')

for user in file_listuser:
	print ""
	print "User : " + user
	user = user.rstrip('\n')
	
	TotalTweets = Get_Total_Tweets(user)
	LastTweets = Get_Last_updated_tweet(user)

	"""
	f=open("last/" + user, "w")
	f.write(TotalTweets)
	f.close()
	"""

	Count = int(TotalTweets) - int(LastTweets)
	
	#print Count
	if (Count == 0 ):
		print "no need to update"
	else:
		GetLinks("http://api.twitter.com/1/statuses/user_timeline.rss?include_entities=false&include_rts=true&count="+ str(Count) +"&screen_name=" + user )
		
		#TODO
		# Store and sort all links
		
	
file_listuser.close()
