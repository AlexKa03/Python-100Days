# Demo: https://appbrewery.github.io/python-day14-demo/

from art import logo, vs
from game_data import data
import random

score = 0

def game(points):
    acc_a = random.choice(data)

    while True:
        print(logo)
        acc_a_followers = acc_a['follower_count']
        acc_b = random.choice(data)
        acc_b_followers = acc_b['follower_count']
        print(f"Compare A: {acc_a['name']}, a {acc_a['description']} from {acc_a['country']} with {acc_a['follower_count']}M followers.")
        print(vs)
        print(f"\nAgainst B: {acc_b['name']}, a {acc_b['description']} from {acc_b['country']}.\n")

        guess = input("Who has more followers? Type 'A' or 'B': ")

        if acc_a_followers > acc_b_followers:
            if guess == 'A':
                points += 1
                print(f"\n" * 40)
                print(f"Correct! Current score is {points}.")
                acc_a = acc_b
            else:
                print(f"\n" * 40)
                print(logo)
                print(f"Incorrect! Final score is {points}.")
                return
        else:
            if guess == 'B':
                points += 1
                print(f"\n" * 40)
                print(f"Correct! Current score is {points}.")
                acc_a = acc_b
            else:
                print(f"\n" * 40)
                print(logo)
                print(f"Incorrect! Final score is {points}.")
                return

game(points=score)
