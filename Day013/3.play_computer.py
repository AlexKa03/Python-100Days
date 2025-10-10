year = int(input("What's your year of birth?"))

# Original Code:
# if year > 1980 and year < 1994:
#     print("You are a millennial.")
# elif year > 1994:
#     print("You are a Gen Z.")

# New Code:
if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994: # Changed from > to >=
    print("You are a Gen Z.")
