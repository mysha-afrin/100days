import random
word_list = ["banana", "apple", "reach", "terminal", "overtime"]
chosen_word = random.choice(word_list)#chooses a word randomly.
print(chosen_word)
lives = 6
place_holder = ""
word_length = len(chosen_word)
for position in range(word_length):
    place_holder += "_"
print(place_holder)
game_over = False
correct_letter = []
while not game_over:
    guess = input("Guess a word:").lower()
    #if guess in chosen_word:
       # correct_letter.append(guess)

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
            lives -= 1
        print(display)

if "_" not in display :
    game_over = True
    print("HUHU, you win!")
else:
    print("Oops, you lost!")