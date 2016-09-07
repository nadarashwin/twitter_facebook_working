#!/usr/local/bin/python2.7
# encoding=utf8

import requests
import key
import time
import json

lim = int(raw_input("whats the number of poss to be retrieved :- "))
def get_posts():
    parameters = {'access_token': key.user_fb_token}
    r = requests.get('https://graph.facebook.com/v2.7/me?fields=posts.limit(%d){id,message,name,from,description,link,message_tags,created_time}' %lim, params=parameters)
    result = json.loads(r.text)
    for i in range(0,lim):
		try:
			print "The created time is :- " + str(result['posts']['data'][i]['created_time'])
			print "The post is :- " + str(result['posts']['data'][i]['name'])
		except IndexError:
			pass
		except:
			print "The post is :- " + str(result['posts']['data'][i]['message'])
get_posts()
