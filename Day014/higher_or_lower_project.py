import art
import game_data
import random

def check_answer(one, two):
    if one > two:
        return "a"
    else:
        return "b"

def game():
    data = game_data.data()
    score = 0
    game_should_continue = True

    print(art.logo)

    profile_two = random.choice(data.profiles)
    while game_should_continue:
        profile_one = profile_two
        profile_two = random.choice(data.profiles)

        # Avoid situation in which we compare the same profile
        while profile_one == profile_two:
            profile_two = random.choice(data.profiles)

        # Display the needed information
        print(f"Compare A: {profile_one["name"]}, a {profile_one["description"]}, from {profile_one["country"]}.\n")
        print(art.vs)
        print(f"Against B: {profile_two["name"]}, a {profile_two["description"]}, from {profile_two["country"]}.")

        # User has to make their guess
        guess = input("Who has more followers? 'A' or 'B' ").lower()

        print("\n"*20)
        print(art.logo)

        # Get profiles followers in variable
        followers_one = profile_one["follower_count"]
        followers_two = profile_two["follower_count"]

        # Gets representation of the profile as 'a' or 'b'
        is_correct = check_answer(followers_one, followers_two)

        if guess == is_correct:
            score += 1
            print(f"You're right! Current score {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_should_continue = False

game()