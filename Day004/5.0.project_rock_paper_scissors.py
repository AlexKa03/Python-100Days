# Demo: https://appbrewery.github.io/python-day4-demo/

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]
index_list = [0, 1, 2]

user_hand = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
game_hand = int(random.choice(index_list))

print(f"Your hand:\n{game_list[user_hand]}")
print(f"Computer chose:\n{game_list[game_hand]}")

if user_hand == game_hand:
    print("It's a DRAW!")
elif user_hand == 0:
    if game_hand == 2:
        print("You WIN!")
    elif game_hand == 1:
        print("You LOSE!")
elif user_hand == 1:
    if game_hand == 0:
        print("You WIN!")
    elif game_hand == 2:
        print("You LOSE!")
elif user_hand == 2:
    if game_hand == 1:
        print("You WIN!")
    elif game_hand == 0:
        print("You LOSE!")
