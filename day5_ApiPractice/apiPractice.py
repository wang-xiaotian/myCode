#!/usr/bin/env python3
import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

resp = requests.get(url)

print(dir(resp.json()))
print(resp.json().keys)

for i in resp.json():
    print(i)

