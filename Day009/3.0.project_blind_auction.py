# Demo: https://appbrewery.github.io/python-day9-demo/

import art

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

def highest_bidder(auction):
    name = ""
    bid = 0.0
    for key in auction:
        if auction[key] > bid:
            name = key
            bid = auction[key]

    # Second solution
    # winner = max(auction, key=auction.get)

    print(f"The winner is {name} with bid of ${bid:.2f}")

auction = {}
print(art.logo)

status = True
while status:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    auction[name] = bid

    other_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if other_bidder == 'no':
        status = False
        highest_bidder(auction)
    else:
        print("\n" * 50)
