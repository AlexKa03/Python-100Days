# Demo: https://appbrewery.github.io/python-day5-demo/

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_list = []

for letter in range(nr_letters):
    password_list.append(random.choice(letters))

for symbol in range(nr_symbols):
    password_list.append(random.choice(symbols))

for symbols in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Easy Version
password_easy = ""
for char in password_list:
    password_easy += char

print(f"Easy version: {password_easy}")

# Hard Version
random.shuffle(password_list)
password_hard = ""
for char in password_list:
    password_hard += char

print(f"Hard version: {password_hard}")
