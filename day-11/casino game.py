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
user_score = calculate_score(user_cards)
def calculate_score(cards):
    """Function to calculate the score of the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)  # Change Ace from 11 to 1
    return sum(cards)