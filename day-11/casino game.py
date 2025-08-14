import random

from art import logo
print(logo[0])

print("Welcome to blackjack!")

def deal_card():
    """Function to deal two random cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

