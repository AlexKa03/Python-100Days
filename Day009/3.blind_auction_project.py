import art

print(art.logo)

auction = {}

other_bidders = True
while other_bidders:
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    auction[name] = int(bid)

    other_bidders = input("Are there any other bidders? Type Y for yes and N for no. ").upper()
    if other_bidders == "Y":
        print("\n" * 25)
    else:
        other_bidders = False

highest_bidder = ""
highest_bid = 0
for bidder in auction:
    if auction[bidder] > highest_bid:
        highest_bidder = bidder
        highest_bid = auction[bidder]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

# DONE-1: Ask the user for input
# DONE-2: Save data into dictionary {name: price}
# DONE-3: Whether if new bids need to be added
# DONE-4: Compare bids in dictionary
