#!/usr/bin/python

import re
import sys 
import urllib2
import xml.dom.minidom
import ExpandUrl


def Get_Total_Tweets(user):
	URL="http://api.twitter.com/1/statuses/user_timeline.xml?include_entities=false&include_rts=true&count=1&screen_name=" + user
	dom = xml.dom.minidom.parse(urllib2.urlopen(URL))
	nodelist=dom.getElementsByTagName("statuses_count")
	return nodelist[0].firstChild.nodeValue

def Get_Last_updated_tweet(user):
	f=open("last/" + user, "r")
	A=f.read().rstrip('\n')
	f.close()
	return A

def GetLinks(url):
	dom = xml.dom.minidom.parse(urllib2.urlopen(url))
	nodelist=dom.getElementsByTagName("description")
	for node in nodelist:
		Get_URL_FromText(node.firstChild.nodeValue)

def Get_URL_FromText(text):
	text = text.replace('\n',' ')
	b=text.split(' ')
	Re = re.compile("http://")
	for x in b:
		m = Re.search(x)
		if m != None:
			try:
				url = ExpandUrl.URLExpander().query(x)
				#print "<p>"+text+"</p><a href='"+url+"'>"+url+"</a>"
				print url
			except:
				print "Unable to Expand url -> "
				try:
					print x
				except:
					print ""

