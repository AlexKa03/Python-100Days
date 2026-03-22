import coffee_maker
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def machine(Menu, CoffeeMaker, MoneyMachine):
    while True:
        command = input("What would you like? (espresso/latte/cappuccino/): ")

        selected_drink = Menu.find_drink(command)

        if selected_drink is None:
            if CoffeeMaker == "report":
                CoffeeMaker.report()
                MoneyMachine.report()
            elif CoffeeMaker == "off":
                return
        else:
            sufficient_resources = CoffeeMaker.enough_resources()


machine(Menu, CoffeeMaker, MoneyMachine)