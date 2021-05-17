from player import Player 
from item import Item

FLASH_LIGHT = Item('flash light', 'lighting the whole room')
MONSTER = Item('monster', 'You can be killed by this monster')
POTION = Item('potion', 'You need this to escape...')
FLOWER = Item('flower', 'Smells really good.')
FRUIT =  Item('fruit', 'Help you to recover')
COOKIE = Item('cookie','You will love this cookie.')
KEY = Item('key', 'You can open the Garden door')

#Global constant values
VALID_COMMANDS = ['go', 'get', 'exit'] # valid commands
INVENTORY = [] #an inventory, which is initially empty
CURRENT_ROOM = 'Hall' # start the player in the Hall

# a dictionary linking a room to other rooms
# A dictionary linking a room to other rooms
# TODO: make room object
ROOMS = {
            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : {FLASH_LIGHT.name : FLASH_LIGHT.description}
                },

            'Kitchen' : {
                  'north' :'Hall',
                  'item'  : {MONSTER.name: MONSTER.description} #TODO add list of items 
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : {POTION.name: POTION.description},
                  'north' : 'Pantry',
                  'east' : 'Living Room'
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'item' : {FLOWER.name : FLOWER.description, FRUIT.name : FRUIT.description}
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : {COOKIE.name : COOKIE.description},
            },
            'Living Room': {
                  'item' : {KEY.name: KEY.description}
            }
         }

''' 
show player's current inventory and position status
output status on console screen
'''
def showStatus():
      #print the player's current status
      print('---------------------------')
      print('You are in the ' + CURRENT_ROOM)
      #print the current inventory
      print('Inventory : ' + str(INVENTORY))
      #print an item if there is one
      if "item" in ROOMS[CURRENT_ROOM]:
            print(f'You see items in {CURRENT_ROOM}:')
            for i in ROOMS[CURRENT_ROOM]['item']:
                  print(i)
      else:
            print(f'This {CURRENT_ROOM} is empty.')
      print("---------------------------")


''' 
helper method: player can take action as (command, content) like ('go', 'north')
return false if player type 'exit game'
return true if plyer types other commands
'''
def userAction(command, content):
    # exit game    
    if command == 'exit':
        if content == 'game':
            print("Bye!")
            return False

    # reference to global variables at very top
    global INVENTORY
    global CURRENT_ROOM
    global ROOMS
    #if they type 'go' first
    if command == 'go':
        #check that they are allowed wherever they want to go
        if content in ROOMS[CURRENT_ROOM]:
        #set the current room to the new room
            CURRENT_ROOM = ROOMS[CURRENT_ROOM][content]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    # fixed get '' 
    if command == 'get':
        #if the room contains an item, and the item is the one they want to get
        if "item" in ROOMS[CURRENT_ROOM] and content in ROOMS[CURRENT_ROOM]['item']:
            #add the item to their inventory
            INVENTORY += [content]
            #display a helpful message
            print(content + ' got!')
            #delete the item from the room
            del ROOMS[CURRENT_ROOM]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + content + '!')

    # other than "exit game", go to next round
    return True

""" 
validate player's command, this game only has 'go', 'get' and 'exit'
return True if the player's command in valid command list
"""
def validUserCommand(command):
    if command.lower() in VALID_COMMANDS:
        return True
    else:
        return False

"""
validate player's command and content
if command not valid or no content, return false
"""
def validUserInput(move):
    valid = True
    if not validUserCommand(move[0]):
        print(f"Valid commands: {VALID_COMMANDS}")
        valid = False
    # prevent receiving get ''. this will add '' in the inventory 
    if len(move) < 2 or (len(move) >= 2  and move[1] == ''):
        print(f"You need type command and content, like 'go _yourDirection_', 'get _yourItem_' or 'exit game'")
        valid = False
    return valid

"""
read player's input from console and get the player's next 'move'
"""
def playerNextMove():
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')
    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.strip().lower().split(" ", 1)
    return move

'''
valid whether to continue or end game
END: if in a same room with a monster
WIN:
CONTINUE: not above condition
'''
def gameContinue():
    ## Define how a player can win
    if CURRENT_ROOM == 'Garden' and 'key' in INVENTORY and 'potion' in INVENTORY:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        return False
    ## If a player enters a room with a monster
    elif 'item' in ROOMS[CURRENT_ROOM] and 'monster' in ROOMS[CURRENT_ROOM]['item']:
        print('A monster has got you... GAME OVER!')
        return False
    else:
        return True

def createPlayer():
      player = Player()
      print(player.name)
