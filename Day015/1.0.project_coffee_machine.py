import sys
from main import MENU, resources

def turn_off(nothing_1, nothing_2, nothing_3):
    sys.exit()

def report(nothing_1, ingredients, nothing_2):
    print("Report:")
    print(f"Water: {ingredients['water']}ml")
    print(f"Milk: {ingredients['milk']}ml")
    print(f"Coffee: {ingredients['coffee']}g")
    print(f"Money: ${ingredients['money']}")

def process_coins():
    quarters = int(input("How many quarters?: ")) # $0.25
    dimes = int(input("How many dimes?: ")) # $0.10
    nickles = int(input("How many nickles?: ")) # $0.05
    pennies = int(input("How many pennies?: ")) # $0.01

    total_coins = round((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)
    print(f"Total Coins: {total_coins:.2f}")
    return total_coins

def check_transaction(inserted_coins, needed_coins):
    if needed_coins == inserted_coins:
        print("Inserted coins are enough, no change option available.")
        return True
    elif needed_coins > inserted_coins:
        print(f"Sorry that's not enough money. ${inserted_coins:.2f} refunded.")
        return False
    else:
        print(f"Here is ${(inserted_coins - needed_coins):.2f} dollars in change")
        return True

def make_coffe(coffe, ingredients, water, milk, coffee, coins):
    ingredients['water'] -= water
    ingredients['milk'] -= milk
    ingredients['coffee'] -= coffee
    ingredients['money'] += coins

    print(f"Here is your {coffe}. Enjoy!")


def process(menu, ingredients, product):
    water_needed = menu[product]['ingredients']['water']
    milk_needed = menu[product]['ingredients']['milk']
    coffee_needed = menu[product]['ingredients']['coffee']
    coins_needed = menu[product]['cost']

    water_available = ingredients['water']
    milk_available = ingredients['milk']
    coffee_available = ingredients['coffee']

    if water_needed <= water_available:
        if milk_needed <= milk_available:
            if coffee_needed <= coffee_available:
                coins_inserted = process_coins()
                transaction_status = check_transaction(coins_inserted, coins_needed)

                if transaction_status:
                    make_coffe(product, ingredients, water_needed, milk_needed, coffee_needed, coins_needed)
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough milk.")
    else:
        print("Sorry there is not enough water.")


def main(menu, ingredients):
    COMMANDS = {
        "off": turn_off,
        "report": report,
        "espresso": process,
        "latte": process,
        "cappuccino": process,
    }

    while True:
        command = input(f"What would you like to order? (espresso/latte/cappuccino): ")

        COMMANDS[command](menu, ingredients, command)

main(MENU, resources)
