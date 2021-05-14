#!/usr/bin/env python3
# by Xander Wang

# imports always go at the top of your code
import requests
import wget
import os

POKEMON_URL =  "https://pokeapi.co/api/v2/pokemon/"

# grab pokenmon data(json) through api
def pickPokemon(name):
    try:
        all_pk = requests.get(POKEMON_URL + name).json()
        return all_pk
    except:
        raise Exception("Couldn't locate your Pokemon")

# download picture of your pokemon
def downLoadPic(pokemon, outfile):
    pic_url = pokemon["sprites"]["front_default"]
    wget.download(pic_url, outfile)
    return os.getcwd() + '\\' + outfile

# return count of game_indices
def indicesCount(pokemon):
    return len(pokemon["game_indices"])

# loop through all move names
def printMoveNames(pokemon):
    for i in pokemon["moves"]:
        print(i['move']['name'])

# reading user input
def userChoicePokemon():
    try:
        userChoice = input("Please type your Pokemon:\n>").lower()
        return userChoice
    except:
        print("Bad happend reading user input.")

def main():
    while True:
        try:
            userInput = userChoicePokemon()
            userPokemon = pickPokemon(userInput)
            pic_location = downLoadPic(userPokemon, f"{userInput}.png")
        
            print('\n' + '-'*100)
            print(f'Pokemon picture saved in: {pic_location}')

            print('\n' + '-'*100)
            print(f'Indices Count: {indicesCount(userPokemon)}')

            print('\n' + '-'*100)
            print("Printing all moves:")
            printMoveNames(userPokemon)
            break
        except:
            print("Try again! Please type your Pokemon:")
            continue
    print("Bye!")

if __name__ == "__main__":
    main()