#!/usr/bin/env python3
def main():
    
    #keep count of how many vamnpires
    count_dracula= 0

    with open("dracula.txt","r") as foo:
        with open("vampytimex.txt","w") as fang:
            for line in foo:
                if "vampire" in line.lower():
                    print(line)
                    count_dracula += 1
                    fang.write(line)

    print(f"this many lines have a vampire:{count_dracula}")

if __name__ == "__main__":
    main()
