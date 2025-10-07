import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, mode):
    result_text = ""
    for char in original_text:
        if char not in alphabet:
            result_text += char
        else:
            if mode == "decode":
                shift_amount *= -1
            result_text += alphabet[(alphabet.index(char) + shift_amount) % 26]
    print(f"Here is the {mode}d result: {result_text}")

should_continue = "Y".upper()

while should_continue == "Y":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, mode=direction)

    should_continue = input("Type Y if you wish to continue using Caesar Cipher or N if you dont: ").upper()

# DONE-1: Import and print the logo from art.py when the program starts.
# DONE-2: What happens if the user enters a number/symbol/space?
# DONE-3: Can you figure out a way to restart the cipher program?
