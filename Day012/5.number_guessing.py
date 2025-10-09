import art
import random
print(art.logo)

def generator():
    return random.randint(1, 100)

def main():
    attempts = 0
    number_to_guess = int(generator())
    difficulty = input(
        "Welcome to the Guess Game!\nI'm thinking of a number between 1 and 100.\nChose difficulty: Type 'easy', 'hard'\n")
    print(f"(You did not saw this, but the number is: {number_to_guess})")

    if difficulty == 'easy':
        attempts = 10
    else:
        attempts = 5
    print(f"You selected {difficulty} difficulty, you have {attempts} attempts to guess the number.")

    while attempts > 0:
        attempts -= 1
        number = input("Make a guess: ")

        if not number.isdigit():
            print(f"Sorry, that's not a number. {attempts} attempts left.")
        elif int(number) > number_to_guess:
            print(f"Too high. {attempts} attempts left.")
        elif int(number) < number_to_guess:
            print(f"Too low. {attempts} attempts left.")
        else:
            print(f"You got it! The number was {number}")
            break

        if attempts == 0:
            print(f"You dont have any attempts left. The number was {number_to_guess} You lost!")
            break

        print("Guess again.")

main()