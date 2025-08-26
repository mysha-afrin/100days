from art import logo, vs
import random
from game_data import data
import os

print(logo[0])

should_continue = True
while should_continue:
    score = 0
    account_a = random.choice(data)
    account_b = random.choice(data)
    if account_a == account_b:
         account_b = random.choice(data)
    def format_data(account):
        #Takes the account data and returns the printable format.
        name = account["name"]
        age = account["age"]
        insta = account["insta"]
        country = account["country"]
        print(f"{name}, a {age} year old, from {country}, {insta}.")


    def check_answer(guess, a_follower_count, b_follower_count):
    #Takes the user guess and follower counts and returns if they got it right.
        if a_follower_count > b_follower_count:
            if guess == "a":
                return True
        else:
            return False
    #ask the user to guess
    print(f"Compare A: {format_data(account_a)}")
    print(vs[0])
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print("\n" * 100)
    a_follower_count = account_a["insta"]
    b_follower_count = account_b["insta"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")