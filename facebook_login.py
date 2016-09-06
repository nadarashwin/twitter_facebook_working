#!/usr/local/bin/python2.7
# encoding=utf8

import requests
from selenium import webdriver
import key
from lxml import html
from bs4 import BeautifulSoup

'''

import facebook

graph = facebook.GraphAPI(key.access_token,version='2.7')

profile = graph.get_object("me")
friends = graph.get_connections("me", "friends")
#graph.put_object("me", "feed", message="I am writing on my wall!")


friend_list = [friend['name'] for friend in friends['data']]
print friend_list
print profile
print graph.get_object("user_events")
'''

__url = "https://www.facebook.com/"
__user = key.user
__pass = key.passw
__email_field = ".//*[@id='email']"
__pass_field = ".//*[@id='pass']"
__login_box = ".//*[@id='u_0_l']"



mydriver = webdriver.Firefox()
mydriver.get(__url)
mydriver.maximize_window()

mydriver.find_element_by_xpath(__email_field).clear()
mydriver.find_element_by_xpath(__email_field).send_keys(__user)


mydriver.find_element_by_xpath(__pass_field).clear()
mydriver.find_element_by_xpath(__pass_field).send_keys(__pass)


mydriver.find_element_by_xpath(__login_box).click()

mydriver.get("https://www.facebook.com/events/birthdays")
count = len(mydriver.find_elements_by_class_name("innerWrap"))

for x in range(0, count):
	text_box = mydriver.find_element_by_tag_name('textarea')
	text_box.send_keys("Happy Birthday cHeeRzzz enjoy!! ")	
	# The birthday message
	time.sleep(5)

