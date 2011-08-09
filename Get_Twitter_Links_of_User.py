#!/usr/bin/python
#By -  Narendra Sisodiya - http://narendrasisodiya.com

from GetTwitterLib import *

user = sys.argv[1]
try :
    count = int(sys.argv[2])
except :
    count = 0

print "User : " + user

if (count <= 0) :
	print "Please enter an integer value of count greater than 0"
else:
	GetLinks("http://api.twitter.com/1/statuses/user_timeline.rss?include_entities=false&include_rts=true&count="+ str(count) +"&screen_name=" + user )
