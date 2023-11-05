import time
import math

player = dict = {"Health":100, "Mana":100, "Stamina":100, "EXP":0}
gp = 0
loc = ""
lp = "None"
le = "None"
purchase = "None"
player_inventory = ["Axe", "Sword", "Buckler"]
player_equips = ["Empty"]
player_body = {"Head": False, "Torso": False, "Gloves":False, "M_Hand": False, "Off_Hand":False, "Dual":False, "Legs": False, "Feet": False}
town = ["Tavern", "Shop", "Church", "Quit"]
Sword = 2, 100, 5, 1
Axe = 4, 90, 6, 1
Leather_Armor = 2, 2, -2
Robes = 0, 0, 2
Potion = "Health", 15
Ether = "Mana", 15
weapon_values = dict = {"Sword":"M_Hand", "Axe":"Dual", "Buckler":"Off_Hand"}
armor_values = [Leather_Armor, Robes]
item_values = {"Potion":("Health", 15), "Ether":("Mana", 10), "Sword":"M_Hand", "Axe":"Dual", "Buckler":"Off_Hand"}
itemequippable = dict = {"Potion":False, "Antidote":False, "Ether":False, "Arrows":False, "Sword":True, "Axe":True, "Bow":True, "Mage Staff":True, "Leather Armor":True, "Iron Chestplate":True, "Robes":True, "Gauntlets":True, "Buckler":True}
shop_items_weapons_t1 = ["Sword", "Axe", "Bow", "Mage Staff"]
shop_items_armor_t1 = ["Leather Armor", "Iron Chestplate", "Robes", "Gauntlets"]
shop_items_items_t1 = ["Potion", "Antidote", "Ether", "Arrows"]
shopvalues = dict = {"Potion":5, "Antidote":5, "Ether":10, "Arrows":10, "Sword":10, "Axe":15, "Bow":5, "Mage Staff":5, "Leather Armor":10, "Iron Chestplate":15, "Robes":5, "Gauntlets":5} #Shop Values
shop_items_enter = ["Weapons", "Armor", "Items", "Leave"]

print(len(player_inventory))
print(weapon_values["Sword"][0])
print(weapon_values["Sword"][1])

print(item_values["Potion"][0])
print(item_values["Potion"][1])
def player_inv():
    global player_inventory
    global gp
    global lp
    global le
    global player_equips
    global loc
    global shopvalues
    global itemequippable
    global player
    global player_body
    equip_ck = ""
    inv_ck = ""
    follow_equip_ck = ""

    while inv_ck == "":
        if len(player_inventory) > 1 and "Empty" in player_inventory:
            player_inventory.remove("Empty")
        elif len(player_inventory) < 1 and "Empty" not in player_inventory and len(player_equips) >= 1:
            player_inventory.append("Empty")
        print('')
        time.sleep(1)
        if "Empty" in player_inventory and gp == 0 and len(player_equips) > 0:
            print("There's nothing in your inventory!")
            loc = ""
            time.sleep(1)
            break
        elif "Empty" in player_inventory and len(player_equips) > 0:
            print("You have",gp,"gp and nothing in your bag!")
            loc = ""
            time.sleep(1)
            break
        elif "Empty" not in player_equips or "Empty" not in player_inventory:
            print("You have:")
            for x in player_inventory:
                print("|"+x+"| ", end="")
            print()
            print("In your inventory.")
            print("")
            print("You have",gp,"gp.")
            print("What would you like to do?")
            print("|Equip| |Unequip| |Use| |Leave|")
            inv_ck = input(">>> ")
            print('')
            if inv_ck == "Leave":
                time.sleep(1)
                print("Okay...")
                inv_ck = ""
                loc = ""
                break
            elif inv_ck == "Equip":
                time.sleep(1)
                while equip_ck == "":
                    print("What would you like to equip?")
                    for x in player_inventory:
                            print(">|"+x+"| ", end="")
                    print()
                    print('')
                    equip_ck = input(">>> ")
                    if equip_ck == "Nothing":
                        time.sleep(1)
                        print("Okay...")
                        equip_ck = ""
                        inv_ck = ""
                        break
                    elif equip_ck in player_inventory:
                        while equip_ck in player_inventory:
                            if equip_ck == lp:
                                lp = ""
                            if itemequippable[equip_ck] == False:
                                print("Cannot wear this item!")
                                equip_ck = ""
                                break
                            if item_values[equip_ck] == "M_Hand" and player_body["M_Hand"] is True:
                                print("Cannot equip! You already have something in your hand!")
                                equip_ck = ""
                                break
                            elif item_values[equip_ck] == "Off_Hand" and player_body["Off_Hand"] is True:
                                print("Cannot equip! You already a=have something in that hand!")
                                equip_ck = ""
                                break
                            elif item_values[equip_ck] == "Dual":
                                if player_body["M_Hand"] == True:
                                    print("Your hands would be full! No!")
                                    equip_ck = ""
                                    break
                                elif player_body["Off_Hand"] == True:
                                    print("Your ahnds would be full! Nawr!")
                                    equip_ck = ""
                                    break
                            player_equips.append(equip_ck)
                            player_inventory.remove(equip_ck)
                            player_body[item_values[equip_ck]] = True
                            if player_body["Dual"] is True:
                                player_body["M_Hand"] = True
                                player_body["Off_Hand"] = True
                            time.sleep(1)
                            print("You equipped the "+equip_ck+"!")
                            le = equip_ck
                            print('')    
                            equip_ck = ""
                            inv_ck = ""
                    else:
                        equip_ck = ""
            elif inv_ck == "Unequip":
                print("Under construction!")
                inv_ck = ""
            elif inv_ck == "Use":
                    while inv_ck == "Use":
                        for x in player_inventory:
                            print("|"+x+"| ", end="")
                        print()
                        print("What would you like to use?")
                        use_ck = input(">>> ")
                        if use_ck in player_inventory:
                            if itemequippable[use_ck] is False:
                                print("Used "+use_ck+"!")
                                stat_ck = item_values[use_ck][0]
                                player[stat_ck] += item_values[use_ck][1]
                                print("You heal",item_values[use_ck][1],stat_ck+"!")
                                player_inventory.remove(use_ck)
                                if use_ck == lp:
                                    lp = ""
                            elif itemequippable[use_ck] is True:
                                print("Cannot consume!")
                        elif use_ck == "Nothing":
                            print("Okay...")
                            use_ck = ""
                            inv_ck = ""
                        else:
                            continue
            else:
                print('')
                inv_ck = ""

    return("Returning...")

def player_stats():
    global player_stats


def it_shop():
    global gp
    global lp
    global loc
    global shop_items_enter
    global shop_items_weapons_t1
    global shop_items_armor_t1
    global shop_items_items_t1
    global shopvalues

    while loc == "Shop":
        time.sleep(1)
        print("Welcome! What are you buying?")
        for x in shop_items_enter:
            print("|"+x+"| ", end="")
        print()
        print('')
        select = input(">>> ")
        while select in shop_items_enter:
            if select == "Leave":
                time.sleep(1)
                print("See you!")
                select = ""
                loc = ""
                break
            if select == "Weapons":
                while select == "Weapons":
                    time.sleep(1)
                    print ("What would you like?")
                    for x in shop_items_weapons_t1:
                        print ("|"+x+"| ", end="")
                    print()
                    print('')
                    purchase = input(">>> ")
                    if purchase in shop_items_weapons_t1:
                        while purchase in shop_items_weapons_t1:
                            purchase_value = shopvalues[purchase]
                            time.sleep(1)
                            print("The",purchase,"is worth",int(purchase_value),"gp. Would you like to buy it?")
                            print('')
                            confirm_purchase = input("Y/N >>> ")
                            if confirm_purchase == "Y":
                                if purchase_value <= gp:
                                    gp = gp - purchase_value
                                    shop_items_weapons_t1.remove(purchase)
                                    player_inventory.append(purchase)
                                    lp = purchase
                                    time.sleep(1)
                                    print("Thank you!")
                                    time.sleep(1)
                                    print("You have",gp,"gp left.")
                                    print('')
                                    confirm_purchase = ""
                                    purchase = ""
                                    break
                                elif purchase_value > gp:
                                    time.sleep(1)
                                    print("Sorry! Not enough gold!")
                                    time.sleep(1)
                                    print("You have",gp, "gp.")
                                    print('')
                                    confirm_purchase = ""
                                    purchase = ""
                                    break
                                else:
                                    time.sleep(1)
                                    print("Something's wrong here...")
                                    print('')
                                    confirm_purchase = ""
                                    continue
                            elif confirm_purchase == "N":
                                time.sleep(1)
                                print("Okay...")
                                print('')
                                confirm_purchase = ""
                                purchase = ""
                                break
                            else:
                                time.sleeep(1)
                                print("Sorry, what was that?")
                                print('')
                                confirm_purchase = ""
                                continue
                    elif purchase == "Nothing":
                        time.sleep(1)  
                        print("Okay...")
                        print('')
                        purchase = ""
                        select = ""
                        break
                    elif "" in shop_items_weapons_t1:
                        time.sleep(1)
                        print ("I'm all out!")
                        print('')
                        purchase = ""
                        select = ""
                        break
                    else:
                        time.sleep(1)
                        print("Not sure if I have that...")
                        print('')
                        purchase = ""
                        continue
        
            elif select == "Armor":
                while select == "Armor":
                    time.sleep(1)
                    print ("What would you like?")
                    for x in shop_items_armor_t1:
                        print ("|"+x+"| ", end="")
                    print()
                    print('')
                    purchase = input(">>> ")
                    if purchase in shop_items_armor_t1:
                        while purchase in shop_items_armor_t1:
                            purchase_value = shopvalues[purchase]
                            time.sleep(1)
                            print("The",purchase,"is worth",int(purchase_value),"gp. Would you like to buy it?")
                            print('')
                            confirm_purchase = input("Y/N >>> ")
                            if confirm_purchase == "Y":
                                if purchase_value <= gp:
                                    gp = gp - purchase_value
                                    shop_items_armor_t1.remove(purchase)
                                    player_inventory.append(purchase)
                                    lp = purchase
                                    time.sleep(1)
                                    print("Thank you!")
                                    time.sleep(1)
                                    print("You have",gp, "gp left.")
                                    print('')
                                    confirm_purchase = ""
                                    purchase = ""
                                    break
                                elif purchase_value > gp:
                                    time.sleep(1)
                                    print("Sorry! Not enough gold!")
                                    time.sleep(1)
                                    print("You have",gp,"gp.")
                                    print('')
                                    confirm_purchase = ""
                                    purchase = ""
                                    break
                                else:
                                    time.sleep(1)
                                    print("Something's wrong here...")
                                    print('')
                                    confirm_purchase = ""
                                    continue
                            elif confirm_purchase == "N":
                                time.sleep(1)
                                print("Okay...")
                                print('')
                                confirm_purchase = ""
                                purchase = ""
                                break
                            else:
                                time.sleep(1)
                                print("Sorry, what was that?")
                                print('')
                                confirm_purchase = ""
                                continue
                    elif purchase == "Nothing":
                        time.sleep(1)
                        print("Okay...")
                        print('')
                        purchase = ""
                        select = ""
                        break
                    else:
                        time.sleep(1)
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
                            purchase_value = shopvalues[purchase]
                            print("The",purchase, "is worth",int(purchase_value),"gp. Would you like to buy it?")
                            print('')
                            confirm_purchase = input("Y/N >>> ")
                            if confirm_purchase == "Y":
                                if purchase_value <= gp:
                                    gp = gp - purchase_value
                                    shop_items_items_t1.remove(purchase)
                                    player_inventory.append(purchase)
                                    lp = purchase
                                    print("Thank you!")
                                    print("You have",gp,"gp left.")
                                    print('')
                                    confirm_purchase = ""
                                    purchase = ""
                                    break
                                elif purchase_value > gp:
                                    print("Sorry! Not enough gold!")
                                    print("You have",gp,"gp.")
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
time.sleep(1)

while loc == "":
    print("")
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
        print(player_inv())
    elif loc == "addgp":
        gp += 10
        print("You have ",gp,"gp.")
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

# SMALL UPDATE BC IM SO TIRED
# STARTED ADDIMG TIME DELAYS TO MAKE IT FEEL A LITTLE MORE REAL

# 10/30
# Started adding Equip system along with adding values to each item. Want to be able to make consumables functional. 