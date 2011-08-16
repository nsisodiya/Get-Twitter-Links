#!/usr/bin/python

import urllib2
import simplejson as json
import sys

class TwitterLib:
    def __init__(self,user):
        URL = "http://api.twitter.com/1/users/show.json?screen_name=" + user + "&include_entities=false"
        try:
            self.userData = json.load(urllib2.urlopen(URL))
        except :
            print "Can't fetch user details..."
            sys.exit(1)

    def get_latest_tweet_id(self):
        return self.userData["status"]["id_str"]

    def get_latest_ripped_tweet_id(self):
        f = open("last/" + self.userData["screen_name"], "r")
        return f.readline().split(":")[1].strip()

    def dump_tweets(self):
        return "\n".join(self.rip_tweeted_links()[-1::-1]) #concatenate backwards

    def dump_resumed_tweets(self):
        return "\n".join(self.resume_ripping_tweets()[-1::-1]) #concatenate backwards

    def resume_ripping_tweets(self):
        tweeted_links = []
        URL = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=" + self.userData["screen_name"] + "&count=200&include_rts=true&include_entities=true&exclude_replies=false&contributor_details=false&trim_user=true&since_id=" + self.get_latest_ripped_tweet_id() + "&page=%d"
        page = 1
        try:
            nodes = json.load(urllib2.urlopen(URL%page))
        except:
            print "Dude check your connectivity / IP blacklisting...I can't even fetch the first page!"
            sys.exit(1)
        while (nodes):
            for node in nodes:
                for link in self.Get_URL_FromTweet(node["entities"]["urls"]):
                    tweeted_links.append(link)
            page+=1
            try:
                nodes = json.load(urllib2.urlopen(URL%page))
            except :
                print "Sorry .... I give up! ... You have some serious issues with your connectivity ... or maybe twitter is over capacity... Try later"
                sys.exit(1)
        return tweeted_links

    def rip_tweeted_links(self):
        tweeted_links = []
        #max_id is required since a user may tweet in between we are ripping
        URL = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=" + self.userData["screen_name"] + "&count=200&include_rts=true&include_entities=true&exclude_replies=false&contributor_details=false&trim_user=true&max_id=" + self.get_latest_tweet_id() + "&page=%d"
        page = 1
        try:
            nodes = json.load(urllib2.urlopen(URL%page))
        except:
            print "Dude check your connectivity / IP blacklisting...I can't even fetch the first page!"
            sys.exit(1)
        while (nodes):
            for node in nodes:
                for link in self.Get_URL_FromTweet(node["entities"]["urls"]):
                    tweeted_links.append(link)
            page+=1
            try:
                nodes = json.load(urllib2.urlopen(URL%page))
            except :
                print "Sorry .... I give up! ... You have some serious issues with your connectivity ... or maybe twitter is over capacity... Try later"
                sys.exit(1)
        return tweeted_links

    def Get_URL_FromTweet(self,urllist):
        tweetlinks = [] #list of links in a particular tweet
        if len(urllist) != 0 :
            for url in urllist: #each element is a dictionary
                if url["expanded_url"] is None:
                    tweetlinks.append(url["url"])
                else:
                    tweetlinks.append(url["expanded_url"]) #TODO: code for expanding URL
        return tweetlinks