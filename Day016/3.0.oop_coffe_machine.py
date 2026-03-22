from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    options = menu.get_items()
    command = str(input(f"What would you like? {options}: "))

    if command == "report":
        coffee_maker.report()
        money_machine.report()
    elif command == "off":
        machine_on = False
    else:
        selected_drink = menu.find_drink(command)
        if coffee_maker.is_resource_sufficient(selected_drink):
            if money_machine.make_payment(selected_drink.cost):
                coffee_maker.make_coffee(selected_drink)
