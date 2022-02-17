MENU = {
    "espresso": {
        "ingredient": {
            "water": 150,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredient": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    }
    ,
    "cappuccino": {
        "ingredient": {
            "water": 150,
            "coffee": 18,
        },
        "cost": 1.5,
    }
}

profit = 0

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def is_Resource_Sufficient(order_ingredient):
    """True order can be made , False when Ingredient is inSufficient"""
    for item in order_ingredient:
        if order_ingredient[item] >= resource[item]:
            print(f"Sorry there is no enough {item}")
            return False
    return True


def isTransaction_Successful(insertedMoney, drinkcost):
    if insertedMoney < drinkcost:
        print("Sorry that's not sufficient . Money Refunded")
        return False
    else:
        change = round(insertedMoney - drinkcost, 2)
        global profit
        profit += insertedMoney - change
        print(f"Here is This Many ${change} in Change")
        return True


def coin_process():
    """Return the Total calculated Coins"""
    print("Please Insert the Coins .")
    total = int(input("Enter How many Quoter ")) * 0.25
    total += int(input("Enter How many Dims ")) * 0.1
    total += int(input("Enter How many Nickel ")) * 0.05
    total += int(input("Enter How many Pannies ")) * 0.01
    return total


def make_coffee(drinkname, orderedingredient):
    for item in orderedingredient:
        resource[item] -= orderedingredient[item]
    print(f"Here is your {drinkname}")

is_on = True
while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water :{resource['water']}")
        print(f"milk :{resource['milk']}")
        print(f"coffee : {resource['coffee']}")
        print(f"Money $ {profit}")
    else:
        drink = MENU[choice]
        if is_Resource_Sufficient(drink["ingredient"]):
            payment = coin_process()
            if isTransaction_Successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredient"])
