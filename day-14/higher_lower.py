from art import logo
from game_data import data
import random
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def format_data(account):
    return f"{account['name']}, a {account['age']} year old, with a net worth of ${account['net worth']} million"
def game():
    score = 0
    game_over = False
    person_a = random.choice(data)
    person_b = random.choice(data)
    while person_a == person_b:
        person_b = random.choice(data)
    while not game_over:
        clear()
        print(logo[0])
        if score == 0:
            print("Welcome to higher lower game!")
        else:
            print(f"You're right! Current score: {score}")
        print(f"Compare A: {format_data(person_a)}")
        print("VS")