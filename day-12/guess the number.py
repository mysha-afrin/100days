import random
print("Welcome to 'Guess the Number'!")
print("I'm thinking of a number between 1 and 100.")
number_to_guess = random.randint(1, 100)
print("Try to guess it!")
print("Choose a difficulty level: 'easy' or 'hard'. Type 'exit' to quit the game.")
difficulty = input("Enter difficulty level: ").lower()
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
elif difficulty == 'exit':
    print("Thanks for playing! Goodbye!")
    exit()
else:
    print("Invalid difficulty level. please try again.")
while attempts > 0:
    print(f"You have {attempts} attempts remaining.")
    guess = input("Make a guess: ")
    if guess.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        exit()
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a valid number.")
        continue
    if guess < 1 or guess > 100:
        print("Your guess is out of range. Please choose a number between 1 and 100.")
        continue
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
        break
    attempts -= 1
    