alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


  # TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# def decrypt(original_text, shift_amount):
      # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#     shifted_text = ""
#     for char in original_text:
#         index = alphabet.index(char)
#         shifted_letter = alphabet[(index - shift_amount) % len(alphabet)]
#         shifted_text += shifted_letter
#
#     print(f"The shifted text is: {shifted_text}")
#
#
# def encrypt(original_text, shift_amount):
#     shifted_text = ""
#     for char in original_text:
#         index = alphabet.index(char)
#         shifted_letter = alphabet[(index + shift_amount) % len(alphabet)]
#         shifted_text += shifted_letter
#
#     print(f"The shifted text is: {shifted_text}")

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'. Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar(original_text, shift_amount, direction):
    shifted_text = ""
    for char in original_text:
        index = alphabet.index(char)
        shift_total = 0
        if direction == "encode":
            shift_total = index + shift_amount
        else:
            shift_total = index - shift_amount
        shifted_letter = alphabet[shift_total % len(alphabet)]
        shifted_text += shifted_letter
    print(f"The shifted text is: {shifted_text}")

# encrypt(original_text=text, shift_amount=shift)
caesar(original_text=text, shift_amount=shift, direction=direction)
