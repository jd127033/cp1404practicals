""" Quick Pick Generator Program"""

import random

NUM_OF_LINES = 6
MAX_NUM = 45
MIN_NUM = 1


quick_pick_count = int(input("How many quick picks? ")) # Ask user for quick pick amount
while quick_pick_count < 0: # Check if the user input is valid
    print("Invalid number of quick picks. Please try again.")
    quick_pick_count = int(input("How many quick picks? "))

for quick_picks in range(quick_pick_count):
    quick_pick = [] # create list for current quick pick.
    for numbers in range(NUM_OF_LINES):
        random_number = random.randint(MIN_NUM, MAX_NUM) # Generate random number within range set by constants.
        while random_number in quick_pick: # Check if the generated number is already in the current quick pick and if so reroll.
            random_number = random.randint(MIN_NUM, MAX_NUM)
        quick_pick.append(random_number) # Add random number to quick pick list.
    quick_pick.sort() # Sort the current quick pick.

    # Using list comprehension, join method and f string formatting to print each quick pick.
    printable_quick_pick = " ".join(f"{random_number:2}" for random_number in quick_pick)
    print(printable_quick_pick)




