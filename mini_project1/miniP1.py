#!/usr/bin/python3

""" Lab 48: MINI PROJECT # 1

What Kdrama should you watch next"""

def main():
    # making sure text is entered with while loop and condition
    choice = ""
    while choice == "":
        choice=input("How do you feel today(sad,mad,excited,like a rebel,happy, or meh)? ").lower()

    # response variable is used to not repeat myself too much
    response = ", so you need to watch."

    # a list of korean shows, I want to update this to a dict where key is mood
    k_list = ["vincinzo","W","start up","nevertheless","itaewan class","Extraordinary Attorney Woo"]

    # if anf elif statements to determine show based on mood, then prints string
    if choice == 'sad':
        print(f"You are feeling {choice}{response} {k_list[1]}")

    elif choice == 'mad':
        print(f"You are feeling {choice}{response} {k_list[0]}")

    elif choice == 'excited':
        print(f"You are feeling {choice}{response} {k_list[2]}")

    elif choice == 'like a rebel':
        print(f"You are feeling {choice}{response} {k_list[4]}")

    elif choice == 'happy':
        print(f"You are feeling {choice}{response} {k_list[5]}")

    elif choice == 'meh':
        print(f"You are feeling {choice}{response} {k_list[3]}")

    else:
        print("watch anime instead")


if __name__ == "__main__":
    main()
