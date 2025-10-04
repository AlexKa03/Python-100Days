print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("Are you going to left or right? (left / right)").lower()
if choice1 == "left":
    choice2 = input("You reached a big river. Are you going to swim or wait for the boat? (swim / wait)")
    if choice2 == "wait":
        choice3 = input("You reached old building. You need to pick which room you are going to- red, blue or yellow? (red / blue / yellow)")
        if choice3 == "yellow":
            print("YOU WIN! You found the long lost Lick King's Frostmourne runeblade!")
        elif choice3 == "red":
            print("YOU LOST! A fire trap has been activated.")
        elif choice3 == "blue":
            print("YOU LOST! The door closed automatically and you were not able to open it, beasts attacked you.")
        else:
            print("You picked a fourth door, never ever seen before, but you were never ever seen again too.")
    elif choice2 == "swim":
        print("YOU LOST! You were attacked by trout.")
    else:
        print("You just got bored of the adventure and went back home.")
elif choice1 == "right":
    print("YOU LOST! You feel in a hidden hole.")
else:
    print("You dont like making an obvious decisions, that's why you just chosen to continue ahead, nor left, nor right- somehow you found Orgrimar.")
