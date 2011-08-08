#!/usr/bin/python
#By -  Narendra Sisodiya - http://narendrasisodiya.com

from urllib import urlopen

import xml.dom.minidom
import re

def Get_Total_Tweets(user):
	URL="http://api.twitter.com/1/statuses/user_timeline.xml?include_entities=false&include_rts=true&count=1&screen_name=" + user
	dom = xml.dom.minidom.parse(urlopen(URL))
	nodelist=dom.getElementsByTagName("statuses_count")
	return nodelist[0].firstChild.nodeValue

print "Initialising User Database"


file_listuser=open('listuser', 'r')

for user in file_listuser:
	user = user.rstrip('\n')
	
	TotalTweets = Get_Total_Tweets(user)
	#TotalTweets = str ( int(TotalTweets) - 7)
	print "User : " + user + " --> " + TotalTweets
	f=open("last/" + user, "w")
	f.write(TotalTweets)
	f.close()
file_listuser.close()
