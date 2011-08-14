#!/usr/bin/python
#By -  Narendra Sisodiya - http://narendrasisodiya.com

from GetTwitterLib import *
import sys

user = sys.argv[1]
try :
    count = int(sys.argv[2])
except :
    count = 0

print "User : " + user

if (count <= 0) :
	print "Please enter an integer value of count greater than 0"
else:
    tweetlinks = GetLinks("http://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rts=true&count=" + str(count) + "&screen_name=" + user)
    for links in tweetlinks:
        print links