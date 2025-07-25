import random
list = ['rock', 'paper', 'scissors']
list_1 = random.choice(list)
print(f"I choose {list_1}.")  # Randomly selects an item from the list
take = input("What do you choose? (rock, paper, scissors): ")
print(f"You chose {take}.")  # User input for choice

if take == list_1:
    print("It's a tie!")
elif (take == 'rock' and list_1 == 'scissors') or (take == 'paper' and list_1 == 'rock') or (take == 'scissors' and list_1 == 'paper'):
    print("You win!")
elif (list_1 == 'rock' and take == 'scissors') or (list_1 == 'paper' and take == 'rock') or (list_1 == 'scissors' and take == 'paper'):
    print("You lose!")