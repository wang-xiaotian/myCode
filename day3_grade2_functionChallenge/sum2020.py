#!/usr/bin/env python3
PUZZLES_DIR = "./day3_grade2_functionChallenge/puzzles.txt"
TARGET = 2020 # target value =? key + value 


def findTwoPuzzles(target):
    result = None;
    dictionaryPuzzles = {}
    try:
        # reading puzzles
        with open(PUZZLES_DIR, 'r') as puzzles:
            for puzzle in puzzles:
                if puzzle.strip().isdigit():
                    if pairPuzzles(dictionaryPuzzles, int(puzzle), target):
                        result = int(puzzle) * (target - int(puzzle))
                        break # the answer has only one pair
                    else:
                        continue
        return result
    except:
        print("Something bad happened")

# if locate the correct pair of values return true, else false 
def pairPuzzles(dictionary, value, target):
    if value in dictionary:
        return True
    else:
        dictionary[target-value] = value 
        return False

# just a quick solution
# need more work
def findThreePuzzles():
    try:
        allValues = []
        with open(PUZZLES_DIR, 'r') as puzzles:
            allValues = puzzles.readlines() # saved in memory; not good for big file
        # loop through all values and use TARGET - value as a target in two puzzles function findTwoPuzzles
        for value in allValues:
            answer = findTwoPuzzles(TARGET - int(value))
            if answer:
                return answer * int(value)
    except:
        print("something bad happend in three puzzels")


answer = findTwoPuzzles(TARGET)
print(f"2 puzzels: The answer is {answer}")

answer = findThreePuzzles()
print(f"3 puzzels: The answer is {answer}")
