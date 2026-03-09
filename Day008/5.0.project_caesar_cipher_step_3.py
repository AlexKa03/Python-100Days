# https://appbrewery.github.io/python-day8-demo/

# TODO-1: Import and print the logo from art.py when the program starts.
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?
def caesar(original_text, shift_amount, direction):
    shifted_text = ""
    for char in original_text:
        if char in alphabet:
            index = alphabet.index(char)
            shift_total = 0
            if direction == "encode":
                shift_total = index + shift_amount
            else:
                shift_total = index - shift_amount
            shifted_letter = alphabet[shift_total % len(alphabet)]
            shifted_text += shifted_letter
        else:
            shifted_text += char
    print(f"The shifted text is: {shifted_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
program_state = True
while program_state:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, direction=direction)

    continue_loop = input("Would you like to continue (y/n)?\n").lower()
    if continue_loop == "n":
        print("Goodbye!")
        program_state = False
