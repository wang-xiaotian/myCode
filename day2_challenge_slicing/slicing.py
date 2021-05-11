#!/usr/bin/env python3
eyes =""
googles = ""
nothing = ""
print(f'My {eyes}! The {googles} do {nothing}')

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
eyes = challenge[2][1]
googles = challenge[2][0]
nothing = challenge[3]
print(f'My {eyes}! The {googles} do {nothing}')

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
eyes = trial[2]["goggles"]
googles = trial[2]["eyes"]
nothing = trial[3]
print(f'My {eyes}! The {googles} do {nothing}')

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]
eyes = nightmare[0]["user"]["name"]["first"]
googles = nightmare[0]["kumquat"]
nothing = nightmare[0]["d"]
print(f'My {eyes}! The {googles} do {nothing}')
