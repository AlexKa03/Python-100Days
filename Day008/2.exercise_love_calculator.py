def calculate_love_score(first_name, second_name):
    true_score = 0
    love_score = 0
    
    for letter in first_name:
        if letter in "true":
            true_score += 1
    
    for letter in second_name:
        if letter in "true":
            true_score += 1
            
    for letter in first_name:
        if letter in "love":
            love_score += 1
    
    for letter in second_name:
        if letter in "love":
            love_score += 1
    
    final_score = true_score * 10 + love_score
    
    print(final_score)

calculate_love_score("Angela Yu", "Jack Bauer") # 53
calculate_love_score("Kanye West", "Kim Kardashian") # 42

name_one = input("What is your name? \n")
name_two = input("What is their name? \n")
calculate_love_score(second_name=name_two, first_name=name_one)
