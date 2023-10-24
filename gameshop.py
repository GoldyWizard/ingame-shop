import math
import time
it_shop = ""
loc = ""
print("You stand in the town square.")
print('')
time.sleep(1)
while loc == "" or loc == "Tavern" or loc == "Brothel" or loc == "Town Square":
    print('Where will you go?')
    time.sleep(1)
    print("|Tavern|     |Shop|      |Brothel|   |Quit|")
    loc = input('>>> ')
    loc = loc.capitalize()
    if loc == "Tavern" or loc == "Brothel":
        time.sleep(1)
        print('They seem to be under construction...')
        print('')
    elif loc == "Shop":
        while it_shop == "" or it_shop == "Weapons" or it_shop == "Armor" or it_shop == "Items":
            time.sleep(1)
            print('')
            print('Welcome to my shop adventurer! Feel free to browse!')
            time.sleep(1)
            print ("|Weapons|   |Armor|   |Items|   |Leave|")
            print('')
            it_shop = input(">>> ")
            it_shop = it_shop.capitalize()
            if it_shop == "Weapons" or it_shop == "Armor" or it_shop == "Items":
                print('')
                time.sleep(1)
                print('Sorry, all out!')
            elif it_shop == "Leave":
                time.sleep(1)
                print ('Bye now!')
                loc = "Town Square"
                time.sleep(1)
            else:
                time.sleep(1)
                print('Is that a dwarven thing?')
                it_shop = ""
    elif loc == "Quit":
        time.sleep(1)
        print('')
        print("Thanks for playing!")
    else:
        time.sleep(1)
        print("No we don't have one of those here...")
        loc = ""

# There might be a better way to do this using T/F flags instead of relying on a variable being a specific value?