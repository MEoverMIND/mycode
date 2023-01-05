#!/usr/bin/env python3
"""Understanding dictionaries
   {key: value, key:value, ...} """

def main():
    """runtime function"""

    ## user input
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n").capitalize()

    # user input
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n").lower()
    
    marvelchars= {
    "Starlord":
    {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
     {"real name": "bruce banner",
     "powers": "super strength",
     "archenemy": "adrenaline"}
             }
    print(f"{char_name}'s {char_stat} is: {marvelchars.get(char_name).get(char_stat)}")


# call our main function
if __name__ == "__main__":
    main()

