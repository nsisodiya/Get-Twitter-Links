#!/usr/bin/python
#By -  Narendra Sisodiya - http://narendrasisodiya.com

import os
from GetTwitterLib import TwitterLib

print "Initialising User Database..."

file_listuser = open('listuser', 'r')

for user in file_listuser:
    user = user.rstrip('\n')
    userObj = TwitterLib(user)
    if not os.path.isfile("last/" + user):
    	print "Initializing " + user + " "
        tweetedLinks = userObj.dump_tweets()
        latestID = userObj.get_latest_tweet_id()
    	f = open("last/" + user, "w")
    	f.write("Latest ID: " + latestID + "\n" + tweetedLinks)
    	f.close()
    else:
        print "Updating " + user + " "
        tweetedLinks = userObj.dump_resumed_tweets()
        latestID = "Latest ID: " + userObj.get_latest_tweet_id()
        f = open("last/" + user, "r+")
        oldID = f.readline() #just in case it's needed somewhere in future
        oldFile = f.read()
        f.seek(0)
        f.write(latestID + "\n" + oldFile + "\n" + tweetedLinks)
        f.close()
file_listuser.close()

print "Initialising Complete..."