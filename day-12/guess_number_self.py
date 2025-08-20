import random

print("Welcome to 'Guess the number'!")
print("I'm thinking of a number between 1 and 100.")
number_to_guess = random.randint(1, 100)
print("Try to guess it!")
print("Choose a difficulty level: 'easy' or 'hard'. Type 'exit' to quit the game.")
difficulty = input("Enter difficulty level: ").lower()
if difficulty == 'easy':
    max_attempts = 10
elif difficulty == 'hard':
    max_attempts = 5
elif difficulty == 'exit':
    print("Thanks for playing! Goodbye!")
    exit()
else:
    print("You have entered invalid")
attempts = 0
while attempts < max_attempts:
    
    
    print(f"You have {max_attempts - attempts} attempts remaining.")
    guess = input("Make a guess:")
    if guess.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        exit()
    attempts += 1
    if not guess:
        print("You didn't enter anything. Please try again.")
        continue
    elif guess.isdigit():
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        if guess < number_to_guess:
            print( "Too low! Try again.")
            if attempts == max_attempts:
                print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
                break
        elif guess > number_to_guess:
            print("Too high! Try again.")
            if attempts == max_attempts:
                print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
                break
        elif guess == number_to_guess:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            break
        elif attempts == max_attempts:
            print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")
            break
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
            break