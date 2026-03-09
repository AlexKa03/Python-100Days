alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    # TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
    #  by the shift amount and print the encrypted text.
    shifted_text = ""
    
    for char in original_text:
        index = alphabet.index(char)
        shifted_letter = alphabet[(index + shift_amount) % len(alphabet)]
        shifted_text += shifted_letter

    print(f"The shifted text is: {shifted_text}")

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
# Did it before I even saw it ;)
# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encrypt(original_text=text, shift_amount=shift)
