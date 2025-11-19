import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry only letters in the english alphabet are allowed.")
        generate_phonetic()
    else:
        print(output_list)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

generate_phonetic()