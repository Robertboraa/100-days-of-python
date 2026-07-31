from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from menu import Menu , MenuItem
go_on = True
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

while go_on:
    option = menu.get_items()
    print("Welcome to Coffee Maker!")
    choice = input(f"Please Make a selection{option}")
    if choice == "off":
        go_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) == True :
            print(money_machine.make_payment(drink.cost))
            print(coffee_maker.make_coffee(drink))
        else :
            print("No resources available.")

