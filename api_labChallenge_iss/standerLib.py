#!/usr/bin/env python3
'''
for people who can only use standard libraries
'''
import urllib.request
import json

URL ='http://api.open-notify.org/astros.json'

webObj = urllib.request.urlopen(URL)
print(type(webObj))
print(dir(webObj))
content = webObj.read()
content_decode = webObj.read().decode("utf-8")
print(f'raw webojb: {content}')
print(f'json read them up: {json.loads(content)}')