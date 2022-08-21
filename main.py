MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def sufficient_resources(drink):
    if resources["water"] >= MENU[drink]["ingredients"]["water"]:
        if resources["milk"] >= MENU[drink]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU[drink]["ingredients"]["coffee"]:
                make_drink(drink)
            else:
                print("Not enough coffee")
        else:
            print("Not enough milk")
    else:
        print("Not enough water")


def make_drink(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
    print(f"Resources left = {resources}")
    drink_price = "{:.2f}".format(MENU[drink]['cost'])
    print(f"Please pay £{drink_price}")


def process_coins(drink):
    quarters = float(input("How many 0.25s have you inserted? ")) * 0.25
    dimes = float(input("How many 0.10s have you inserted? ")) * 0.10
    nickles = float(input("How many 0.05s have you inserted? ")) * 0.05
    pennies = float(input("How many 0.01s have you entered? ")) * 0.01
    resources["money"] += quarters + dimes + nickles + pennies
    "{:.2f}".format( resources["money"])
    print(f"Total money = £{resources['money']}")
    if resources["money"] == MENU[drink]["cost"]:
        give_coffee(drink)
        print("Perfect amount")
        resources["money"] - MENU[drink]["cost"]
    elif resources["money"] > MENU[drink]["cost"]:
        profit = "{:.2f}".format(resources["money"] - MENU[drink]["cost"])
        resources["money"] - MENU[drink]["cost"]
        print(f"You have given £{profit} extra")
        give_coffee(drink)
    else:
        print("Sorry there is not enough money")
        return


def report():
    total_water = (resources["water"])
    total_milk = (resources["milk"])
    total_coffee = (resources["coffee"])
    total_money = (resources["money"])
    print(f"Resources remaining:\nWater = {total_water}ml,\nMilk = {total_milk}ml,\nCoffee = {total_coffee}g,"
          f"\nMoney = £{total_money}")


def give_coffee(drink):
    print(f"Enjoy your {drink}!")
    return


def make_coffee():
    machines_on = True
    while machines_on:
        drink_choice = input("Hi, would you like an espresso, latte or cappuccino ? ")
        if drink_choice == "report":
            report()
        elif drink_choice == "off":
            machines_on = False
        else:
            sufficient_resources(drink_choice)
            process_coins(drink_choice)


make_coffee()
