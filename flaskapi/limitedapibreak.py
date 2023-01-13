#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   SOLUTION 01 - How quickly can we get to 50 requests (per hour) to be rate limited
   by FlaskLimiter? Run the script to get results."""

import time
import requests

URI = "http://localhost:2224/"

def main():

    # get the current time
    start_time = time.time()

    # start an infinite loop
    while True:
        r = requests.get(f"{URI}fast")  # this URI is limited by 50 lookups per hour
        if r.status_code != 200:
            end_time = time.time()
            break # stop looping, as we have hit the limit

    # display the total time it took to perform the lookups
    print(f"To reach the limit of /fast, it took {end_time - start_time} seconds")

# invoke the main function
if __name__ == "__main__":
    main()

