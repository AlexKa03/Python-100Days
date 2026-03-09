# 💪 This is a difficult challenge! 💪 
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times 
# R occurs 1 time 
# U occurs 2 times 
# E occurs 2 times 
# Total = 5 
# L occurs 1 time 
# O occurs 0 times 
# V occurs 0 times 
# E occurs 2 times 
# Total = 3 
# Love Score = 53

# Example Input 
# calculate_love_score("Kanye West", "Kim Kardashian")
# Example Output
# 42

# How to test your code and see your output?
# Udemy coding exercises do not have a console, so you cannot use the input() function. You will need to call your function with hard-coded values like so:
# def calculate_love_score(name1, name2):
#   # your code here
# # Call your function with hard coded values
# calculate_love_score("Kanye West", "Kim Kardashian")

def calculate_love_score(name1, name2):
    true_check = "true"
    love_check = "love"
    
    true_check_score = 0
    love_check_score = 0
    
    both_names = name1.lower() + name2.lower()
    
    for letter in both_names:
        for char in true_check:
            if letter == char:
                true_check_score += 1
    
    for letter in both_names:
        for char in love_check:
            if letter == char:
                love_check_score += 1 
    
    love_score = (true_check_score * 10) + love_check_score
    print(love_score)
    
calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score("Angela Yu", "Jack Bauer")
