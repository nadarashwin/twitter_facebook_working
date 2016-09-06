#!/usr/local/bin/python2.7
# encoding=utf8


import facebook
import key

graph = facebook.GraphAPI(key.access_token,version='2.7')

profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")
#graph.put_object("me", "feed", message="I am writing on my wall!")


friend_list = [friend['name'] for friend in friends['data']]
print friend_list
print profile
print graph.get_object("user_events")
