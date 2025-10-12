import time
import random

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(ingredients):
    """Returns True if the ingredients are sufficient."""
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}. Call technician.")
            return False
        return True

def process_payment():
    """Returns the total of inserted coins"""
    print("Please insert coins:")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))

    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total

def is_transaction_success(payment_received, drink_cost):
    """Returns True if the transaction was successful."""
    animation_loading("transaction")
    if payment_received >= drink_cost:
        change = round(payment_received - drink_cost, 2)
        print(f"Here is your change: ${change}!")
        global money
        money += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink, drink_ingredients):
    """Deduct the required ingredients from the resources and prints the coffee is made."""
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    animation_loading("making")
    print(f"Here is your {drink} ☕️. Enjoy!")

def animation_loading(type_of):
    """Animation"""
    symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    i = 0

    # random duration between 3–10 seconds
    duration = random.randint(3, 7)
    start_time = time.time()

    # run animation until the time runs out
    while time.time() - start_time < duration:
        i = (i + 1) % len(symbols)
        if type_of == "transaction":
            print('\r\033[KProcessing payment %s' % symbols[i], flush=True, end='')
        else:
            print('\r\033[KMaking your coffee %s' % symbols[i], flush=True, end='')
        time.sleep(0.1)
    print()

is_on = True
while is_on:
    choice = input("What would you like to drink? (espresso/ latte/ cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml.\n"
              f"Milk: {resources['milk']}ml.\n"
              f"Coffee: {resources['coffee']}g.\n"
              f"Money: ${money}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_payment()
            if is_transaction_success (payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid choice")
