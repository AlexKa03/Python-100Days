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

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors)")

print(player_choice)
if player_choice == '0':
    print(rock)
elif player_choice == '1':
    print(paper)
else:
    print(scissors)

computer_choice = random.randint(0, 2)

if computer_choice == 0: #ROCK
    print(f"Computer chose\n{rock}")
    if player_choice == '0':
        print("It's a Tie!")
    elif player_choice == '1':
        print("You Loose!")
    else:
        print("You Win!")
elif computer_choice == 1: #PAPER
    print(f"Computer chose\n{paper}")
    if player_choice == '0':
        print("You Win!")
    elif player_choice == '1':
        print("It's a Tie!")
    else:
        print("You Loose!")
else: #SCISSORS
    print(f"Computer chose\n{scissors}")
    if player_choice == '0':
        print("You Loose!")
    elif player_choice == '1':
        print("You Win!")
    else:
        print("It's a Tie!")
