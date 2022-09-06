from data import MENU, resources


def check_enough(choice):
    water = resources["water"] - MENU[choice]["ingredients"]["water"]
    milk = resources["milk"] - MENU[choice]["ingredients"]["milk"]
    coffee = resources["coffee"] - MENU[choice]["ingredients"]["coffee"]
    check = {"water": water, "milk": milk, "coffee": coffee}
    if water < 0 or milk < 0 or coffee < 0:
        print("Sorry there is not enough resources.")
        return "fail"
    else:
        return check


def calc_coins(quarters, dimes, nickels, pennies):
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return round(total, 2)


def calc_price(choice):
    return MENU[choice]["cost"]


def print_resources():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} ml")
    print(f"Money: ${money}")

on = True
money = 0
while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print_resources()
    elif choice == "off":
        on = False
    elif not check_enough(choice) == "fail":
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        if calc_coins(quarters, dimes, nickels, pennies) >= calc_price(choice):
            change = calc_coins(quarters, dimes, nickels, pennies) - calc_price(choice)
            money += calc_price(choice)
            print(f"Here is ${change} in change.")
            print(f"Here is your {choice} ☕️. Enjoy!")
            left_over = check_enough(choice)
            resources["water"] = left_over["water"]
            resources["milk"] = left_over["milk"]
            resources["coffee"] = left_over["coffee"]
        else:
            print("Sorry that's not enough money. Money refunded.")