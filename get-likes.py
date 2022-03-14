#!/usr/bin/python3
import json
import codecs
from instagram_private_api import Client

username = ''
password = ''

def from_json(json_object):
    if '__class__' in json_object and json_object['__class__'] == 'bytes':
        return codecs.decode(json_object['__value__'].encode(), 'base64')
    return json_object

with open('creds-' + username + '.json') as file_data:
	cached_settings = json.load(file_data, object_hook=from_json)

api = Client(username, password, settings=cached_settings)
results = api.feed_liked()
likes = results['items']
next = results['next_max_id']

while next:
	results = api.feed_liked(max_id=next)
	likes.extend(results['items'])
	next = results.get('next_max_id')

with open('likes.json', 'w') as outfile:
	json.dump(likes, outfile)
