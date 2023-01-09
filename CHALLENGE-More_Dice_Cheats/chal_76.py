#!/usr/bin/python3
"""RZFeeser | Alta3 Research
Creating a simple dice program utilizing classes."""


# imports from cheadice.py (this is in the local directory)
from cheatdice import Player
from cheatdice import Cheat_Swapper
from cheatdice import Cheat_Loaded_Dice
from cheatdice import Cheater_Deebo

def main():
    """run-time code"""

    # create two cheater objects
    cheater1 = Cheat_Swapper() # ability is to change 3rd dice roll to 6
    cheater2 = Cheat_Loaded_Dice() # increase all rolls by +1 provided they are < 6
    player1 = Player()
    deebo = Cheater_Deebo() 

    # both players take turns
    cheater1.roll()
    cheater2.roll()

    #deebo vs regular player
    player1.roll()
    deebo.roll()
    print(f"Player 1 rolled {player1.get_dice()}")
    print(f"deebo rolled {deebo.get_dice()}")

    
    if sum(player1.get_dice()) == sum(deebo.get_dice()):
    
        print("Draw!")

    elif sum(player1.get_dice()) > sum(deebo.get_dice()):
        deebo.cheat(player1)
        print(f"these your dice homie! {player1.get_dice()}")
        print(f"and these are mine {deebo.get_dice()}")
        print("looks like i won again punk")

    else:
        print("deebo wins: Where my money")



    

if __name__ == "__main__":
    main()

