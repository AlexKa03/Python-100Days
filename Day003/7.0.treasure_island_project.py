# Your goal today is to build a "Chose your own adventure game". Using what you have learnt in the lessons today you will be building a very simple version of this type of text game.
# Use the flow chart linked here to create the game logic.
# Once you've completed the project, you can always extend the game and make it more interesting!
# Demo: https://appbrewery.github.io/python-day3-demo/

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

decision1 = input("You reached a crossroad. Ar you going Left or Right? ").lower()
if decision1 == "left":
    decision2 = input("You reached a small dock. How are you going to reach the other end? Are you going to Wait or Swim? ").lower()
    if decision2 == "wait":
        decision3 = input("You entered old house. There are 3 doors? Are you going trough Red, Blue or Yellow? ").lower()
        if decision3 == "yellow":
            print("Good Good Good Good Good Good! You found the treasure! YOU WIN !")
        elif decision3 == "red":
            print("You were burned alive by the fire! GAME OVER !")
        elif decision3 == "blue":
            print("You were eaten by beasts ! GAME OVER!")
        else:
            print("You chose the only option that does not exist and you broke the space and time continuum! GAME OVER!")
    else:
        print("You were attacked by trout! GAME OVER !")
else:
    print("You fell into a gole! GAME OVER !")