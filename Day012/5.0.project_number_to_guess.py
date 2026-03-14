# Demo: https://appbrewery.github.io/python-day12-demo/

import art
import random

ATTEMPTS = 0

def number_generator():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)

def add_attempts():
    difficulty = input("Choose a difficulty. Type 'easy' for 10 attempts or 'hard' for 5 attempts: ")

    global ATTEMPTS
    if difficulty == "easy":
        ATTEMPTS = 10
    else:
        ATTEMPTS = 5

def game():
    number_to_guess = number_generator()
    global ATTEMPTS

    print(art.logo)
    print("I'm thinking of a number (int) between 1 and 100.")
    print(f"Dev mode: The number is {number_to_guess}.")

    add_attempts()

    while ATTEMPTS != 0:
        guess = int(input("Make a guess: "))
        if guess == number_to_guess:
            print(f"You got it! The answer was {number_to_guess}.")
            return
        elif guess < number_to_guess:
            ATTEMPTS -= 1
            print(f"Your guess is too low. You have {ATTEMPTS} attempts remaining.")
        elif guess > number_to_guess:
            ATTEMPTS -= 1
            print(f"Your guess is too high. You have {ATTEMPTS} attempts remaining.")

    if ATTEMPTS == 0:
        print(f"You've run out of guesses. The answer was {number_to_guess}.")

game()
