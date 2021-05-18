#!/usr/bin/env python3
import argparse   # pull in arguments from CLI
import requests
import time
import hashlib
from pprint import pprint

CREDS_FILE = './api_lab_marvel/marvel.priv'
API = 'http://gateway.marvel.com/v1/public/characters'

# return credential api-key from a creadential file
def getCredential(file):
    with open(file) as creds:
        nasaCreds = creds.readlines()
    tokens = {}
    for line in nasaCreds:
            keys = line.strip('\n').split('=')
            tokens[keys[0]] = keys[1]
    return tokens

'''
hash our key as md5(ts+privateKey + publicKey)
'''
def hashBuilder(rand, privkey, pubkey):
    return hashlib.md5((f"{rand}{privkey}{pubkey}").encode('utf-8')).hexdigest()


def marvelCharCall(rand, keyhash, pubkey, lookmeup):
    r = requests.get(f"{API}?name={lookmeup}&ts={rand}&apikey={pubkey}&hash={keyhash}")  # send an HTTP GET to this location
    # the marvel APIs are "flakey" at best, so check for a 200 response
    if r.status_code != 200:
        response = None     #
    else:
        response = r.json()
    # return the HTTP response with the JSON removed
    return response

def main():
    print(args.hero)
    keys = getCredential(CREDS_FILE)
    rand = str(time.time()).rstrip('.')
    keyHash = hashBuilder(rand, keys['PRIVATE_KEY'], keys['PUBLIC_KEY'])
    response = marvelCharCall(rand, keyHash, keys['PUBLIC_KEY'], 'hero') #call api with input character
    pprint(response)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    ## This allows us to pass the lookup character
    parser.add_argument('--hero', help='Character to search for within the Marvel universe')
    args = parser.parse_args()
    print(args)
    main()