# Demo: https://appbrewery.github.io/python-day11-demo/
# Checklist: https://listmoz.com/view/6h34DJpvJBFVRlZfJvxF

import random
import art

def deal_card():
    """Returns random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(hand):
    """Takes a list of cards, returns their score and checks if we have initial BlackJack."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)

def compare(p_score, c_score):
    """Takes user score and computer score and returns True if they have the same score."""
    if p_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, the computer has BlackJack 😱"
    elif p_score == 0:
        return "Win with BlackJack 😎"
    elif p_score > 21:
        return "Lose, you busted by going over 21 😭"
    elif c_score > 21:
        return "Win, the computer busted by going over 21 🤗"
    elif p_score > c_score:
        return "Win, your hand has higher score 👌"
    elif p_score < c_score:
        return "Lose, the computer has higher score 😑"

def game():
    print("Welcome to Blackjack!")
    print(art.logo)
    player_hand = []
    computer_hand = []
    player_score = -1
    computer_score = -1
    is_game_over = False

    for i in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {player_hand}, and your score is {player_score}.")
        print(f"Computer's first card: {computer_hand[0]}.")

        if computer_score == 0 or player_score == 0 or player_score > 21:
            is_game_over = True
        else:
            new_card = input(f"Type 'y' to get another card, or type 'n' to pass: ").lower()
            if new_card == 'y':
                player_hand.append(deal_card())
            elif new_card == 'n':
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"You final hand: {player_hand}, and your score is {player_score}.")
    print(f"Computer's final hand: {player_hand}, and computer's score is {player_score}.")
    print(compare(player_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' for Yes or 'n' for no ").lower() == "y":
    print("\n" * 30)
    game()
