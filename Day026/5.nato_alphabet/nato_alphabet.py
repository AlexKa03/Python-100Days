import pandas

#DONE-1. Create a dictionary in this format:
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in alphabet.iterrows()}

#DONE-2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ").upper()
user_input = [letter for letter in user_input]
translated_word = [alphabet[letter] for letter in user_input]

print(translated_word)