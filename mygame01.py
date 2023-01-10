#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""
import random

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
      quit
    ''')

def rps():
  options=['rock','paper','scissor']
  name=input("Enter your name :")
  MonsterScore=0 
  PlayerScore=0
  NumberOfRounds=0
  gameOn=True
  print(f"Welcome {name.title()} youve run into a monster and not must play them in a game of RPS!")
  while NumberOfRounds<3:
    MonsterOption=random.choice(options)
    PlayerOption=input("Enter rock/ paper/ scissor :").lower()
    print(f"Monster Option :{MonsterOption}")
    print(f"{name.title()} option :{PlayerOption}")
    NumberOfRounds += 1
    if MonsterOption==PlayerOption:
      print('Tie')
    elif (MonsterOption=='rock' and PlayerOption == 'scissor') or (MonsterOption=='scissor' and PlayerOption=='paper') or (MonsterOption=='paper' and PlayerOption=='rock'):
      print("Monster wins")
      MonsterScore += 1
    elif (PlayerOption=='rock' and MonsterOption == 'scissor') or (PlayerOption=='scissor' and MonsterOption=='paper') or (PlayerOption=='paper' and MonsterOption=='rock'):
      print(f"{name.title()} wins")
      PlayerScore += 1
    else:
      print("Choose a valid option to play this game.") 
    print("-------------------------")
    print("")
    print(f"Round No: {NumberOfRounds}")
    print("------ Score Board ------")
    print(f"{name.title()}: {PlayerScore} | Monster: {MonsterScore}")
    print("===============================")
    print("")
    if NumberOfRounds==3:
      gameOn=False
      break
  if PlayerScore==MonsterScore:
    print("You live but the monster lives too, but i cant let you leave this room!")
    quit()
  elif PlayerScore>MonsterScore:
    print(f"Congrats {name.title()}, You defeated the monster!!")
    del rooms[currentRoom]['item']
  else:
    print(f"Dang the monster wins and you lose the game!! Better luck next time {name.title()}!")
    quit()

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
      print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")




# an inventory, which is initially empty
inventory = []

## A dictionary linking a room to other rooms
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : 'key'
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'item' : 'potion'
               },
            'Garden' : {
                    'east': 'Rainbow World',
                    'north' : 'Dining Room',
                    'item': 'unicorn'
            },
            'Rainbow World' : {
                    'west':'Garden',
                    'item':'Emerald Tablet'

         }
     }


# start the player in the Hall
currentRoom = 'Hall'

showInstructions()

# breaking this while loop means the game is over
while True:
    showStatus()

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':  
        move = input('>')
    
    if move == 'quit'.lower():
        quit()

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            #add the item to their inventory
            inventory.append(move[1])
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item key:value pair from the room's dictionary
            del rooms[currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

        # If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        rps()

        ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

        ## Define how a player can win
    if currentRoom == 'Rainbow World' and 'unicorn' in inventory:
        print(r""" You Freed the unicorn. Fly Fly Away!

                                ,`,`,`,`,
          . . . .               `\`\`\`\;
          `\`\`\`\`,            ~|;!;!;\!
           ~\;\;\;\|\          (--,!!!~`!       .
          (--,\\\===~\         (--,|||~`!     ./
           (--,\\\===~\         `,-,~,=,:. _,//
            (--,\\\==~`\        ~-=~-.---|\;/J,
             (--,\\\((```==.    ~'`~/       a |
               (-,.\\('('(`\\.  ~'=~|     \_.  \
                  (,--(,(,(,'\\. ~'=|       \\_;>
                    (,-( ,(,(,;\\ ~=/        \
                    (,-/ (.(.(,;\\,/          )
                     (,--/,;,;,;,\\         ./------.
                       (==,-;-'`;'         /_,----`. \
               ,.--_,__.-'                    `--.  ` \
              (='~-_,--/        ,       ,!,___--. \  \_)
             (-/~(     |         \   ,_-         | ) /_|
             (~/((\    )\._,      |-'         _,/ /
              \\))))  /   ./~.    |           \_\;            
           ,__/////  /   /    )  /
            '===~'   |  |    (, <.
                     / /       \. \
                   _/ /          \_\
                  /_!/            >_\


""")
        break
