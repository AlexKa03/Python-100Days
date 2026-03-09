import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
game_state = True
previous_correct = []
while game_state:
    guess = input("Guess a letter: ").lower()

    display = ""

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.
    for letter in chosen_word:
        if letter in previous_correct:
            display += letter
        elif letter == guess:
            previous_correct.append(letter)
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        print("!YOU WON!")
        game_state = False
