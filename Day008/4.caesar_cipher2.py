alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def decrypt(original_text, shift_amount):
#     decrypted_text = ""
#     for char in original_text:
#         index = alphabet.index(char)
#         decrypted_text += alphabet[(index - shift_amount) % 26]
#     print(f"Here is the decoded result: {decrypted_text}")
#
# def encrypt(original_text, shift_amount):
#     encrypted_text = ""
#     for char in original_text:
#         index = alphabet.index(char)
#         encrypted_text += alphabet[(index + shift_amount) % 26]
#     print(f"Here is the encoded result: {encrypted_text}")

def caesar(original_text, shift_amount, mode):
    result_text = ""
    for char in original_text:
        if mode == "decode":
            shift_amount *= -1
        result_text += alphabet[alphabet.index(char) + shift_amount % 26]
    print(f"Here is the {mode}d result: {result_text}")

caesar(original_text=text, shift_amount=shift, mode=direction)

# DONE-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# DONE-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# Done-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'. Use the value of the user chosen 'direction' variable to determine which functionality to use.
