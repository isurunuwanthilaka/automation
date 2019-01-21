# -*- coding: cp1252 -*-
from fbchat import Client
from fbchat.models import *
import time

username = "username"
password = "password"
client =Client(username, password)

users = client.fetchAllUsers()
t=0
for user in users:
    try:
        text = '''message'''
        client.send(Message(text),user.uid)
        time.sleep(2)
        t+=1
        print user.name + " message sent successfully"
        break
    except(Exception):
        print user.name + " message not sent"

#   for i in ls:
#    name = i
#    friend = client.searchForUsers(name)[0]
#    text = 'Hello'
#    client.send(Message(text),friend.uid)

print t
client.logout()
