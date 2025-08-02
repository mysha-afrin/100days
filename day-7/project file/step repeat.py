import random
word_list = ["soikot", "mango", "banana", "apple", "terminal", "telegram", "world", "syntax"]
chosen_word = random.choice(word_list)
print(chosen_word)
place_holder = ""
world_length = len(chosen_word)
for position in range(world_length):
    place_holder += "_"
print(place_holder)


game_over = False
correct_letter = []
while not game_over:
    guess = input("Guess a word:").lower()
    

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    print(display)
    if "_" not in display:
        print("You win!")