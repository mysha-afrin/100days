from machine_data import data
from resoures import in_stock
import os
while True:
    print("\n" * 200)
    print("Welcome to the virtual coffee machine!")
    print("Here is our menu:")
    for item in data:
        name = item['name']
        coffee = item['coffee']
        water = item['water']
        milk = item['milk']
        price = item['price']
        print(f"{name}, ${price}")
        print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    print(f"Here is ${total} in total.")
    if total < price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        print("Here is your coffee. Enjoy!")
    change = total - price
    print(f"Here is ${change} in change.")
    for item in in_stock:
        item['water'] -= water
        item['milk'] -= milk
        item['coffee'] -= coffee
    print(f"Water left: {item['water']}ml")
    print(f"Milk left: {item['milk']}ml")
    print(f"Coffee left: {item['coffee']}g")
    if item['water'] <= 0 or item['milk'] <= 0 or item['coffee'] <= 0:
        print("Sorry, we are out of stock.")
        break