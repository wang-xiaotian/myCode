#!/usr/bin/dev python3

import urllib.request
import datetime
import json
import pprint

APOD_API_URL = 'https://api.nasa.gov/planetary/apod?api_key='
ASTD_API_URL = 'https://api.nasa.gov/neo/rest/v1/feed?api_key='

CRED_FILE = './api_lab19_asteroid/nasa.creds'

# return credential api-key from a creadential file
def getCredential(file):
    with open(file) as creds:
        nasaCreds = creds.read()
    return nasaCreds.strip('\n')

# display get response 
def displayGetRequestNasa(url, credFile, query):
    nasaCreds = getCredential(credFile)
    api = url + nasaCreds + query
    print(api)
    apodurObj = urllib.request.urlopen(api)
    # print(f'reponse code: {apodurObj.code}')
    # print(f'reponse message: {apodurObj.msg}')
    # print(f'reponse length: {apodurObj.length}')

    apod = json.loads(apodurObj.read().decode('utf-8'))
    #pprint.pprint(apod)
    return apod

# read date from user
def userInputDate(type):
    while True:
        userInput = input(f"Please enter {type} date yyyy-mm-dd: \n>")
        try:
            date = datetime.datetime.strptime(userInput, '%Y-%m-%d')
            return date.date()
        except:
            print('Invalid date formate.')
            continue

def queryNasaStartEnd(api, credFile):
    startDate = userInputDate("Start")
    #endDate = userInputDate("End")
    query = f'&start_date={startDate}'
    return displayGetRequestNasa(ASTD_API_URL, CRED_FILE, query)

def largestId():
    apod = queryNasaStartEnd(ASTD_API_URL, CRED_FILE)
    largestId = 0
    for a in apod:
        print(a)
    print(f'Element count: {apod["element_count"]}')
    for i in apod["near_earth_objects"]:
        print(i)
        for j in apod['near_earth_objects'][i]:
            print(int(j['id']))
            if int(j['id']) > largestId:
                largestId = int(j['id'])
    print(f'Largest Id: {largestId}')
    

def main():
    largestId()


    #displayGetRequestNasa(ASTD_API_URL, CRED_FILE,'&start_date=2010-01-01&end_date=2020-01-01')

if __name__ == "__main__":
    main()


