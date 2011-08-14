#!/usr/bin/python
#By -  Narendra Sisodiya - http://narendrasisodiya.com

import os
from GetTwitterLib import TwitterLib

print "Initialising User Database..."

file_listuser=open('listuser', 'r')

for user in file_listuser:
    user = user.rstrip('\n')
    if not os.path.isfile("last/" + user):
    	print "Initializing " + user + " "
        userObj = TwitterLib(user)
    	f=open("last/" + user, "w")
    	f.write(userObj.dump_tweets())
    	f.close()
file_listuser.close()

print "Initialising Complete..."