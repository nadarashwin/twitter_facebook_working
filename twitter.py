#!/usr/local/bin/python2.7
# encoding=utf8

import requests
import json
import key
from requests_oauthlib import OAuth1

api = "https://api.twitter.com/1.1/"
auth = OAuth1(key.con_key, key.con_sec, key.acc_tok, key.acc_sec)

def timeline():
	url = requests.get("%s/statuses/user_timeline.json" %api, auth = auth)
	print "Your profile name is :- " + str(url.json()[0]['user']['name'])
	print "Your location is set as :- " + str(url.json()[0]['user']['location'])
	print "Your account was created on :- " + str(url.json()[0]['user']['created_at'])
	print "Your url is mentioned as :- " + str(url.json()[0]['user']['entities']['url']['urls'][0]['expanded_url'])
	print "Total count of tweets are :- " + str(url.json()[0]['user']['statuses_count'])
	print "Total count of following are :- " + str(url.json()[0]['user']['friends_count'])
	print "Total count of followers are :- " + str(url.json()[0]['user']['followers_count'])

timeline()

