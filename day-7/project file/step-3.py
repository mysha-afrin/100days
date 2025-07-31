import random
#word list
word_list = ["banana", "mango", "apple", "bungi", "grape", "grave", "python", "reached"]
#pick a word
chosen_word = random.choice(word_list)
guessed_letter = []
lives = 6
print(chosen_word)

#Initial display
print("Welcome to hangman")
print("_" * len(chosen_word))

#Game loop
while lives > 0:
    guess = input("Guess a letter :").lower()
    if guess in guessed_letter:
        print("You already guessed the word.")
        continue
    guessed_letter.append(guess)
    if guess in chosen_word:
        print("Correct!")
    else:
        lives -=1
        print("Oops")
#display the guess
    display = ""
    for letter in chosen_word:
        if letter in guessed_letter:
            display += letter + ""
        else:
            display = "_"
        print(display)
    if  all(letter in guessed_letter for letter in chosen_word):
        print("🎉 You win!")
        break

    else:
        print(f"You lost .The word was {chosen_word}")