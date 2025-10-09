import art
import random

def print_cards_blackjack(player, computer):
    print(f"Your cards: {player}, current score: {sum(player)}")
    print(f"Computer's first card: {computer}, current score: {sum(computer)}")
    return

def print_cards_end(player, computer):
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
    return

def if_ace(p_cards):
    index = 0
    for card in p_cards:
        if card == 11:
            p_cards[index] = 1
        index += 1
    return p_cards

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_continues = True
new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while new_game == "y":
    print("\n"*20)
    print(art.logo)

    player_cards = [random.choice(cards), random.choice(cards)]
    computer_cards = [random.choice(cards), random.choice(cards)]

    if sum(computer_cards) == 21:
        print_cards_blackjack(player_cards, computer_cards)
        print("The computer has blackjack!\nYou lose!")
    elif sum(player_cards) == 21:
        print_cards_blackjack(player_cards, computer_cards)
        print("You have blackjack!\nYou win!")
    else:
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")

        new_card = input("Type 'y' to get another card, type 'n' to pass: ")

        while new_card == "y":
            player_cards.append(random.choice(cards))

            if 11 in player_cards and sum(player_cards) > 21:
                player_cards = if_ace(player_cards)

            if sum(player_cards) > 21:
                new_card = "n"
                print_cards_end(player_cards, computer_cards)
                print("You went over.\nYou lose!")
                game_continues = False
            else:
                print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
                print(f"Computer's first card: {computer_cards[0]}")
                new_card = input("Type 'y' to get another card, type 'n' to pass: ")

        if game_continues:
            while sum(computer_cards) < 17:
                computer_cards.append(random.choice(cards))

            print_cards_end(player_cards, computer_cards)
            if sum(computer_cards) > 21:
                print(f"The computer went over.\nYou win!")
            elif sum(player_cards) > sum(computer_cards):
                print(f"Your score is greater than the computer's.\nYou win!")
            elif sum(player_cards) == sum(computer_cards):
                print(f"You have the same score as the computer.\nIt's a tie!")
            else:
                print(f"The computer score is greater than yours.\nYou lose!")

    new_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")