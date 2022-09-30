from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

turn_off = False

while not turn_off:

    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        turn_off = True
    elif menu.find_drink(choice) is None:
        break
    else:
        drink_choice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink_choice):
            if money_machine.make_payment(drink_choice.cost):
                coffee_maker.make_coffee(drink_choice)
