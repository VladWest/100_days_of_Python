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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def show_resources(list_resources):
    for resource in list_resources:
        print(f"{resource} = {list_resources[resource]}")

# TODO: 4. Check if resources sufficient


def make_coffee(user_input, list_of_resources, menu):
    """This function take user choice and check if resources sufficient returns cost of chosen coffee or error if not"""
    if user_input == "espresso":
        if list_of_resources["water"] >= menu["espresso"]["ingredients"]["water"]:
            list_of_resources["water"] -= menu["espresso"]["ingredients"]["water"]
            list_of_resources["coffee"] -= menu["espresso"]["ingredients"]["coffee"]
            return menu["espresso"]["cost"]
        else:
            return 0
    elif user_input == "latte":
        if list_of_resources["water"] >= menu["latte"]["ingredients"]["water"]:
            list_of_resources["water"] -= menu["latte"]["ingredients"]["water"]
            list_of_resources["milk"] -= menu["latte"]["ingredients"]["milk"]
            list_of_resources["coffee"] -= menu["latte"]["ingredients"]["coffee"]
            return menu["latte"]["cost"]
        else:
            return 0
    elif user_input == "cappuccino":
        if list_of_resources["water"] >= menu["cappuccino"]["ingredients"]["water"]:
            list_of_resources["water"] -= menu["cappuccino"]["ingredients"]["water"]
            list_of_resources["milk"] -= menu["cappuccino"]["ingredients"]["milk"]
            list_of_resources["coffee"] -= menu["cappuccino"]["ingredients"]["coffee"]
            return menu["cappuccino"]["cost"]
        else:
            return 0

# TODO: 6. Process coins


def money_count(price_of_coffee, resources_left):
    print("Please, insert the coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if price_of_coffee > total:
        return 0
    else:
        total -= price_of_coffee
        total = round(total, 2)
        if "money" in resources_left:
            resources_left["money"] += price_of_coffee
        else:
            resources_left["money"] = 0
            resources_left["money"] += price_of_coffee
        return total


should_continue = True
while should_continue:
    # TODO: 1. Ask user to input what they want to
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO: 2. Create report command
    if user_choice == "report":
        show_resources(resources)
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        coffee_cost = make_coffee(user_input=user_choice, list_of_resources=resources, menu=MENU)
        if coffee_cost == 0:
            print("Sorry there are not enough water in tank")
            should_continue = False
        else:
            # TODO: 3. Ask about money
            count = money_count(coffee_cost, resources)
            # TODO: 7. Check transaction
            if count == 0:
                print("Sorry you put not enough money")
                should_continue = False
            else:
                print(f"Here is ${count} in change.")
                print(f"Here is your {user_choice} ☕. Enjoy!")

    # TODO: 5. Create "off" command to power off machine
    elif user_choice == "off":
        print("powering off...")
        should_continue = False
    else:
        print("Wrong choice")
