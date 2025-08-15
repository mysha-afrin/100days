import random

from art import logo
print(logo[0])

print("Welcome to blackjack!")

def deal_card():
    """Function to deal two random cards."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computers_card = []
for _ in range(2):
    #using under score with for loop to indiczte that we don't need the loop variable
    #deal two cards to user and computer
    
    user_cards.append(deal_card())
    computers_card.append(deal_card())