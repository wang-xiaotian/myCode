#!/usr/bin/env python3
PUZZLES_DIR = "./day3_grade2_functionChallenge/puzzles.txt"
TARGET = 2020 # target value =? key + value 


def findTwoPuzzles():
    result = None;
    dictionaryPuzzles = {}
    try:
        # reading puzzles
        with open(PUZZLES_DIR, 'r') as puzzles:
            for puzzle in puzzles:
                if puzzle.strip().isdigit():
                    if pairPuzzles(dictionaryPuzzles, int(puzzle)):
                        result = int(puzzle) * (TARGET - int(puzzle))
                        break # the answer has only one pair
                    else:
                        continue
        if result:
            print(f"Found answer: {result}")
        else:
            print(f"Cannot find two entries that sum to {TARGET}")
    except:
        print("Something bad happened")

# if locate the correct pair of values return true, else false 
def pairPuzzles(dictionary, value):
    print(value)
    if value in dictionary:
        return True
    else:
        dictionary[TARGET-value] = value 
        return False

findTwoPuzzles()