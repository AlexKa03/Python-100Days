year = int(input("What's your year of birth? "))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year >= 1994: # add >=, since the year 1994 was outside all if-else checks
    print("You are a Gen Z.")
