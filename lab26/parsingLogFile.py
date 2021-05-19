#!/usr/bin/env python3
LOG_DIR = "./lab26/keystone.common.wsgi"



def basicReadLines():
    getCount = 0 # number of GET requests
    postCount = 0 # number of POST requests
    # open file
    keystoneFile = open(LOG_DIR, "r")
    # list of lines in memory
    keystoneFileLines = keystoneFile.readlines()
    # loop over lines
    for l in keystoneFileLines:
        if "- - - - -] POST" in l:
            postCount += 1
        elif "- - - - -] GET" in l:
            getCount += 1
    keystoneFile.close()
    print(f"GET requests: {getCount}")
    print(f'POST requests: {postCount}')


def advanceStreamReading():
    getCount = 0 # number of GET requests
    postCount = 0 # number of POST requests
    with open(LOG_DIR, 'r') as keystoneFile:
        for l in keystoneFile:
            if "- - - - -] POST" in l:
                postCount += 1
            elif "- - - - -] GET" in l:
                getCount += 1
    keystoneFile.close()
    print(f"GET requests: {getCount}")
    print(f'POST requests: {postCount}')

basicReadLines()
advanceStreamReading()

