#!/usr/local/bin/python2.7
# encoding=utf8

import requests
import key
import time
import json
import dateutil.parser as dateparser


lim = int(raw_input("whats the number of poss to be retrieved :- "))
parameters = {'access_token': key.user_fb_token}
fb_api = ("https://graph.facebook.com/v2.7")
def get_posts():
    r = requests.get('%s/me?fields=posts.limit(%d){id,message,name,from,description,link,message_tags,created_time}' %(fb_api,lim), params=parameters)
    result = json.loads(r.text)
    for i in range(0,lim):
		try:
		#	print "The created time is :- " + str(result['posts']['data'][i]['created_time'])
			print "The post is :- " + str(result['posts']['data'][i]['name'])
			print "The description is :- " + str(result['posts']['data'][i]['description'])
			print "The created time is :- " + dateparser.parse(result['posts']['data'][0]['created_time']).strftime('%d/%B/%Y %H:%M:%S')
		except IndexError:
			pass
		except KeyError:
			pass
		except:
			print "The post is :- " + str(result['posts']['data'][i]['message'])

def friend_lists():
    	r = requests.get('%s/me?fields=friendlists{name}' %(fb_api), params=parameters)
	result = json.loads(r.text)
	for i in range(0,len(result['friendlists']['data'])):
		print "The name of the friendlist is :- " + str(result['friendlists']['data'][i]['name'])

get_posts()
friend_lists()
