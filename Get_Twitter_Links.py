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
	print "Updating User : " + user + "..."
	user = user.rstrip('\n')

	TotalTweets = Get_Total_Tweets(user)
	LastLinkCount,LastTweetID = Get_Last_updated_details(user)

	Count = int(TotalTweets) - int(LastTweetCount) #number of tweets to fetch

	if (Count == 0 ):
		print "Already up to date"
	else:
		print "Fetching new links..."
		tweetedlinks = GetLinks("http://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&count="+ str(Count) +"&screen_name=" + user)
		f = open("last/"+user,"a")
        f.writelines(tweetedlinks)
        f.close()

file_listuser.close()

print "Successfully updated ..."
