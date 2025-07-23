def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")

def transaction(type):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01

    cost = MENU[type]["cost"]

    if total >= cost:
        change = total - cost
        resources["money"] += cost
        print(f"Here is ${change} in change.")
        print(f"Here is your espresso ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")

def check_resources(type):
    coffee = MENU[type]
    ingredients = coffee["ingredients"]

    if type == "espresso":
        return resources["water"] >= ingredients["water"] and resources["coffee"] >= ingredients["coffee"]
    elif type == "latte":
        return resources["water"] >= ingredients["water"] and resources["coffee"] >= ingredients["coffee"] and resources["milk"] >= ingredients["milk"]
    else:
        return resources["water"] >= ingredients["water"] and resources["coffee"] >= ingredients["coffee"] and resources["milk"] >= ingredients["milk"]

def espresso():
    ingre = MENU["espresso"]["ingredients"]
    resources["water"] -= ingre["water"]
    resources["coffee"] -= ingre["coffee"]

def latte():
    ingre = MENU["latte"]["ingredients"]
    resources["water"] -= ingre["water"]
    resources["coffee"] -= ingre["coffee"]
    resources["milk"] -= ingre["milk"]

def cap():
    ingre = MENU["cappuccino"]["ingredients"]
    resources["water"] -= ingre["water"]
    resources["coffee"] -= ingre["coffee"]
    resources["milk"] -= ingre["milk"]

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
    "money" : 0
}

isOff = False

while not isOff:
    userInp = input("What would you like? (espresso/latte/cappuccino): ")
    if userInp == "off":
        isOff = True
    elif userInp == "report":
        report()
    else:
        possible = check_resources(userInp)
        if possible:
            transaction(userInp)
            if userInp == "espresso":
                espresso()
            elif userInp == "latte":
                latte()
            else:
                cap()
        else:
            ingre = MENU[userInp]["ingredients"]
            for item in ingre:
               if ingre[item] > resources[item]:
                   print(f"Sorry there is not enough {item}")
                   break

