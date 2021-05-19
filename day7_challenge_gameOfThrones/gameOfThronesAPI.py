#!/usr/bin/python3
import requests
import pprint
import numpy as np

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        books = [] # list of books
        proBooks = [] # list of pro books
        allegs = [] # list of allegs

        for i in got_dj:
            booksAPIs = i['books'] #book apis
            povBooksAPIs = i['povBooks'] #probook apis
            allegiancesAPIs = i['allegiances'] 
            #if len(booksAPIs) > 0:
            books.extend(infoCollector(booksAPIs, 'name'))
            proBooks.extend(infoCollector(povBooksAPIs, 'name'))
            allegs.extend(infoCollector(allegiancesAPIs, 'name'))

        print(f'books: {books}')
        print(f'proBooks: {proBooks}')
        print(f'allegs: {allegs}')


'''
helper method that collect field inforamtion from APIs
return a list of collected information
'''
def infoCollector(apis, field):
    result = []
    for api in apis: 
        response = requests.get(api)
        responseJson = response.json()
        result.append(responseJson[field])
    return result

if __name__ == "__main__":
        main()
