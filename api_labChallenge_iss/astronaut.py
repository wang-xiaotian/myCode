#!/usr/bin/env python3

import requests

#URL
URL = 'http://api.open-notify.org/astros.json'

'''
return json format respose of get request
'''
def getAstronaut(url):
    try:
        return requests.get(url).json()
    except:
        print('Failed get request')

'''
print astronauts status on console
'''
def printAstronauts(response):
    print(f'People in Space: {response["number"]}')
    for people in response['people']:
        print(f'{people["name"]} is on the {people["craft"]}')

def main():
    response = getAstronaut(URL)
    printAstronauts(response)

if __name__ == "__main__":
    main()
