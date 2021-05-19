#!/usr/bin/python3
import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        pprint.pprint(got_dj)

        print(f'Name: {got_dj["name"]}')

        booksAPIs = got_dj['books'] #book apis
        allegiancesAPIs = got_dj['allegiances'] 

        #if len(booksAPIs) > 0:
        books = infoCollector(booksAPIs, 'name')
        allegs = infoCollector(allegiancesAPIs, 'name')

        print(books)
        print(allegs)


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
