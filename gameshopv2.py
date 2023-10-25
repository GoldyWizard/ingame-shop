import math
import time
it_shop = ""
it_sweapons = ["Sword", "Axe", "Bow"]
Sword = ()
Axe = 15
Bow = 5
it_sarmor = ["Leather Armor", "Iron Chestplate", "Robe"]
it_sitems = ["Potion", "Cheese Wheel", "Bundle of Arrows x10"]
inventory = []
purchase = ""
loc = ""
gp = 100
print("You stand in the town square.")
print('')
time.sleep(1)
while loc == "":
    print('')
    print('Where will you go?')
    time.sleep(1)
    print("|Tavern|     |Shop|      |Brothel|   |Quit|")
    loc = input('>>> ')
    loc = loc.capitalize()
    if loc == "Tavern" or loc == "Brothel":
        time.sleep(1)
        print('They seem to be under construction...')
        print('')
        loc = ""
    elif loc == "Shop":
        while it_shop == "":
            time.sleep(1)
            print('')
            print('Welcome to my shop adventurer! Feel free to browse!')
            time.sleep(1)
            print ("|Weapons|   |Armor|   |Items|   |Leave|")
            print('')
            it_shop = input(">>> ")
            it_shop = it_shop.capitalize()
            if it_shop == "Weapons":
                while it_shop == "Weapons":
                    print('')
                    print("What would you like?")
                    time.sleep(1)
                    for x in it_sweapons:
                        print("|"+x+"| ", end="")
                    print()
                    print('')
                    time.sleep(1)
                    purchase = input(">>> ")
                    purchase = purchase.capitalize()
                    if purchase == "Nothing":
                        time.sleep(1)
                        print('')
                        print("Okay...")
                        it_shop = ""
                        purchase = ""
                    elif purchase == "":
                        continue
                    elif purchase in it_sweapons:
                        time.sleep(1)
                        print('')
                        print("Thank you!")
                        it_sweapons.remove(purchase)
                        print(it_sweapons)
                        purchase = ""
                    elif purchase not in it_sweapons:
                        time.sleep(1)
                        print('')
                        print("Not sure I have that...")
                        purchase = ""
            elif it_shop == "Armor":
                while it_shop == "Armor":
                    print('')
                    print("What would you like?")
                    time.sleep(1)
                    for x in it_sarmor:
                        print("|"+x+"| ", end="")
                    print()
                    print('')
                    time.sleep(1)
                    purchase = input(">>> ")
                    purchase = purchase.capitalize()
                    if purchase == "Nothing":
                        time.sleep(1)
                        print('')
                        print("Okay...")
                        it_shop = ""
                        purchase = ""
                    elif purchase == "":
                        continue
                    elif purchase in it_sarmor:
                        time.sleep(1)
                        print('')
                        print("Thank you!")
                        it_sarmor.remove(purchase)
                        print(it_sarmor)
                        purchase = ""
                    elif purchase not in it_sarmor:
                        time.sleep(1)
                        print('')
                        print("Not sure I have that...")
                        purchase = ""
            elif it_shop == "Items":
                while it_shop == "Items":
                    print('')
                    print("What would you like?")
                    time.sleep(1)
                    for x in it_sitems:
                        print("|"+x+"| ", end="")
                    print()
                    print('')
                    time.sleep(1)
                    purchase = input(">>> ")
                    purchase = purchase.capitalize()
                    if purchase == "Nothing":
                        time.sleep(1)
                        print('')
                        print("Okay...")
                        it_shop = ""
                        purchase = ""
                    elif purchase == "":
                        continue
                    elif purchase in it_sitems:
                        time.sleep(1)
                        print('')
                        print("Thank you!")
                        it_sitems.remove(purchase)
                        print(it_sitems)
                        purchase = ""
                    elif purchase not in it_sitems:
                        time.sleep(1)
                        print('')
                        print("Not sure I have that...")
                        purchase = ""
            elif it_shop == "Leave":
                time.sleep(1)
                print('')
                print ('Bye now!')
                loc = ""
                it_shop = ""
                time.sleep(1)
                break
            elif it_shop == "":
                continue
            else:
                time.sleep(1)
                print('Is that a dwarven thing?')
                it_shop = ""
    elif loc == "Quit":
        time.sleep(1)
        print('')
        print("Thanks for playing!")
    elif loc == "":
        continue
    else:
        time.sleep(1)
        print("No we don't have one of those here...")
        loc = ""

# There might be a better way to do this using T/F flags instead of relying on a variable being a specific value?