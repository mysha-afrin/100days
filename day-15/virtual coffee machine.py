from machine_data import data
from resoures import in_stock
import os
print("Welcome to the virtual coffee machine!")
print("Here is our menu:")
for item in data:
    name = item['name']
    coffee = item['coffee']
    water = item['water']
    milk = item['milk']
    price = item['price']
    print(f"{name}, ${price}")