#!/usr/bin/python3
from utility import showStatus, playerNextMove, validUserInput, userAction, gameContinue, createPlayer


'''
This a RPG game:
1. allows user to move to different rooms 
2. collects items if the user's current room has at least one item

'''
def running():
    #loop forever until use type 'exit game' or player in an END game condition
    while True:
        showStatus()
        move = playerNextMove() # collect player's input
        # input validation
        if not validUserInput(move): 
            continue
        # does player want to exit game?
        if not userAction(move[0], move[1]):
            break
        # game in an end condition?
        if not gameContinue():
            break

'''
greeting message and instructions of how to play this game
output message on console screen
'''
def showInstructions():
  #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
    go [direction]
    get [item]
    ''')


'''
execute this game by showing instruction first then interacting with player until the END
'''
def gameExecute():
    showInstructions() # greeting message
    running()

def main():
    gameExecute()

if __name__ == "__main__":
    main()