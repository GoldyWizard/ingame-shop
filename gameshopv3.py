import time
import math
gp = 100
loc = ""
lp = "0"
purchase = ""
player_inventory = ["Empty"]
town = ["Tavern", "Shop", "Church", "Quit"]
shop_items_weapons_t1 = ["Sword", "Axe", "Bow", "Mage Staff"]
shop_items_armor_t1 = ["Leather Armor", "Iron Chestplate", "Robes", "Gauntlets"]
shop_items_items_t1 = ["Potion", "Antidote", "Ether", "Arrows"]
dict = {"Potion":5, "Antidote":5, "Ether":10, "Arrows":10, "Sword":10, "Axe":15, "Bow":5, "Mage Staff":5, "Leather Armor":10, "Iron Chestplate":15, "Robes":5, "Gauntlets":5} #Shop Values
shop_items_enter = ["Weapons", "Armor", "Items", "Leave"]

def it_shop():
    global gp
    global lp
    global loc
    global shop_items_enter
    global shop_items_weapons_t1
    global shop_items_armor_t1
    global shop_items_items_t1
    global dict

    while loc == "Shop":
        print("Welcome! What are you buying?")
        for x in shop_items_enter:
            print("|"+x+"| ", end="")
        print()
        print('')
        select = input(">>> ")
        while select in shop_items_enter:
            if select == "Leave":
                print("See you!")
                print('')
                select = ""
                loc = ""
                break
            if select == "Weapons":
                while select == "Weapons":
                    print ("What would you like?")
                    for x in shop_items_weapons_t1:
                        print ("|"+x+"| ", end="")
                    print()
                    print('')
                    purchase = input(">>> ")
                    if purchase in shop_items_weapons_t1:
                        while purchase in shop_items_weapons_t1:
                            purchase_value = dict[purchase]
                            print("The ",purchase,"is worth ",int(purchase_value),"gp. Would you like to buy it?")
                            print('')
                            confirm_purchase = input("Y/N >>> ")
                            if confirm_purchase == "Y":
                                if purchase_value <= gp:
                                    gp = gp - purchase_value
                                    shop_items_weapons_t1.remove(purchase)
                                    player_inventory.append(purchase)
                                    print("Thank you!")
                                    print("You have ",gp,"gp left.")
                                    print('')
                                    confirm_purchase = ""
                                    purchase = ""
                                    break
                                elif purchase_value > gp:
                                    print("Sorry! Not enough gold!")
                                    print("You have ",gp, "gp.")
                                    print('')
                                    confirm_purchase = ""
                                    purchase = ""
                                    break
                                else:
                                    print("Something's wrong here...")
                                    print('')
                                    confirm_purchase = ""
                                    continue
                            elif confirm_purchase == "N":
                                print("Okay...")
                                print('')
                                confirm_purchase = ""
                                purchase = ""
                                break
                            else:
                                print("Sorry, what was that?")
                                print('')
                                confirm_purchase = ""
                                continue
                    elif purchase == "Nothing":
                        print("Okay...")
                        print('')
                        purchase = ""
                        select = ""
                        break
                    elif "" in shop_items_weapons_t1:
                        print ("I'm all out!")
                        print('')
                        purchase = ""
                        select = ""
                        break
                    else:
                        print("Not sure if I have that...")
                        print('')
                        purchase = ""
                        continue
        
            elif select == "Armor":
                while select == "Armor":
                    print ("What would you like?")
                    for x in shop_items_armor_t1:
                        print ("|"+x+"| ", end="")
                    print()
                    print('')
                    purchase = input(">>> ")
                    if purchase in shop_items_armor_t1:
                        while purchase in shop_items_armor_t1:
                            purchase_value = dict[purchase]
                            print("The ",purchase, "is worth ",int(purchase_value),"gp. Would you like to buy it?")
                            print('')
                            confirm_purchase = input("Y/N >>> ")
                            if confirm_purchase == "Y":
                                if purchase_value <= gp:
                                    gp = gp - purchase_value
                                    shop_items_armor_t1.remove(purchase)
                                    player_inventory.append(purchase)
                                    lp = purchase
                                    print("Thank you!")
                                    print("You have ",gp, "gp left.")
                                    print('')
                                    confirm_purchase = ""
                                    purchase = ""
                                    break
                                elif purchase_value > gp:
                                    print("Sorry! Not enough gold!")
                                    print("You have ",gp,"gp.")
                                    print('')
                                    confirm_purchase = ""
                                    purchase = ""
                                    break
                                else:
                                    print("Something's wrong here...")
                                    print('')
                                    confirm_purchase = ""
                                    continue
                            elif confirm_purchase == "N":
                                print("Okay...")
                                print('')
                                confirm_purchase = ""
                                purchase = ""
                                break
                            else:
                                print("Sorry, what was that?")
                                print('')
                                confirm_purchase = ""
                                continue
                    elif purchase == "Nothing":
                        print("Okay...")
                        print('')
                        purchase = ""
                        select = ""
                        break
                    else:
                        print("Not sure if I have that...")
                        print('')
                        purchase = ""
                        continue
        
            elif select == "Items":
                while select == "Items":
                    print ("What would you like?")
                    for x in shop_items_items_t1:
                        print ("|"+x+"| ", end="")
                    print()
                    print('')
                    purchase = input(">>> ")
                    if purchase in shop_items_items_t1:
                        while purchase in shop_items_items_t1:
                            purchase_value = dict[purchase]
                            print("The ",purchase, "is worth ",int(purchase_value),"gp. Would you like to buy it?")
                            print('')
                            confirm_purchase = input("Y/N >>> ")
                            if confirm_purchase == "Y":
                                if purchase_value <= gp:
                                    gp = gp - purchase_value
                                    shop_items_items_t1.remove(purchase)
                                    player_inventory.append(purchase)
                                    print("Thank you!")
                                    print("You have ",gp,"gp left.")
                                    print('')
                                    confirm_purchase = ""
                                    purchase = ""
                                    break
                                elif purchase_value > gp:
                                    print("Sorry! Not enough gold!")
                                    print("You have ",gp,"gp.")
                                    print('')
                                    confirm_purchase = ""
                                    purchase = ""
                                    break
                                else:
                                    print("Something's wrong here...")
                                    print('')
                                    confirm_purchase = ""
                                    continue
                            elif confirm_purchase == "N":
                                print("Okay...")
                                print('')
                                confirm_purchase = ""
                                purchase = ""
                                break
                            else:
                                print("Sorry, what was that?")
                                print('')
                                confirm_purchase = ""
                                continue
                    elif purchase == "Nothing":
                        print("Okay...")
                        print('')
                        purchase = ""
                        select = ""
                        break
                    else:
                        print("Not sure if I have that...")
                        print('')
                        purchase = ""
                        continue

            else:
                print("What was that?")
                print('')
                select = ""
    return "Returning..."                
print("You stand in town square.")
print("")

while loc == "":
    print("Where would you like to go?")
    for x in town:
        print ("|"+x+"| ", end="")
    print()
    print('')
    loc = input(">>> ")
    if loc in town:
        if loc == "Shop":
            print(it_shop())
            loc = ""
        elif loc == "Tavern":
            print("Oh they're closed right now.")
            loc = ""
        elif loc == "Church":
            print("No it's not Sunday yet...")
            loc = ""
        elif loc == "Leave":
            print("See you next time!")
            loc = ""
            break
    elif loc == "ck":
        if lp in player_inventory and "Empty" in player_inventory:
            player_inventory.remove("Empty")
        for x in player_inventory:
            print("|"+x+"|")
        print()
        print('')
        loc = ""
    else:
        print("Where???")
        loc = ""
        continue



# player_gp = 100
# dict = {"Potion":50, "Sword":75, "Shield":125}
# print("Welcome to the item shop.")
# print("What do you want?")
# def item_shop():
#     shopitems = ["Potion", "Sword", "Shield"]
#     return shopitems
# shop = item_shop()
# print(shop)
# purchase = input(">>> ")
# if purchase in item_shop():
#     print("You have purchased a ", purchase)
#     if purchase in dict:
#         purchase = dict[purchase]
#     print("You have ", player_gp-int(purchase), "gold pieces left.")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////|
# Quit game command.                                                                                                    [X]                            ///
# Try to implement a save at some point?                                                                                [ ]                            ///
# Add more classes                                                                                                      [ ]                            ///
# Add equipment                                                                                                         [ ]                            ///
# Add NPCS                                                                                                              [ ]                            ///
# Add colored text                                                                                                      [ ]                            ///
# Clean up the code if you can                                                                                          [ ]                            ///
# Make the code loop after game ends, so the program won't quit                                                         [X]                            ///
# Add sound effects for the spots where you have to wait for the command line. ex: when killed by butcher               [ ]                            ///
# Add inventory system                                                                                                                                 ///
# Add enemies to fight                                                                                                                                 ///
# Possibly add graphics                                                                                                                                ///
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////|