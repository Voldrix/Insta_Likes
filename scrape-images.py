#!/usr/bin/python3

import os
import json
import shutil
import pathlib
import requests
import hashlib
from datetime import datetime, timedelta
requests.urllib3.disable_warnings()

DIR = 'images/'

with open('likes.json') as file_data:
	likes = json.load(file_data)

if not os.path.isdir(DIR + '/profiles'):
	pathlib.Path(DIR + '/profiles').mkdir(parents=True, exist_ok=True)

def download(url, name):
	if not os.path.isfile(DIR + name):
		try:
			r = requests.get(url, stream=True, timeout=(4,None), verify=False)
		except:
			print('Error getting: ' + source + ' (skipping)')
			return
		if r.status_code != 200:
			print(r.url + ' :: ' + str(r.status_code))
			return
		with open(DIR + name, 'wb') as f:
			r.raw.decode_content = True
			shutil.copyfileobj(r.raw, f)
		r.close()

for like in likes:
	postdate = datetime.utcfromtimestamp(int(like['taken_at'])).strftime('%Y-%m-%d')
	filename = postdate + '_' + like['user']['username'] + '_' + like['code']
	if 'carousel_media' in like:
		suffix = 0
		for img in like['carousel_media']:
			#extension = img['image_versions2']['candidates'][0]['url'].split('?')[0].split('.')
			#ext = '.' + extension[len(extension)-1]
			download(img['image_versions2']['candidates'][0]['url'], filename + '-' + str(suffix) + '.jpg')
			suffix += 1
	else:
		#extension = like['image_versions2']['candidates'][0]['url'].split('?')[0].split('.')
		#ext = '.' + extension[len(extension)-1]
		download(like['image_versions2']['candidates'][0]['url'], filename + '.jpg')
	#profile pic
	download(like['user']['profile_pic_url'], 'profiles/' + like['user']['username'] + '.jpg')

