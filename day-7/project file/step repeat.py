import random
from hangman_word import word_list
from hangman_art import logo, stages
#from hangman_art import stages

#word_list = ["algorithm", "elepant", "biologist", "happiness", "", "telegram", "notebook", "rainbow", "beautiful", "adventure", "stronger", "education", "Knowledge"]
print(logo)
lives = 6
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
            print(f"You already guessed {guess}")
        else:
            display += "_"
            


    print(display)
    if guess not in chosen_word:
        lives -= 1
        if lives == 6:
            print(stages[0])
        elif lives == 5:
            print(stages[1])
        elif lives == 4:
            print(stages[2])
        elif lives == 3:
            print(stages[3])
        elif lives == 2:
            print(stages[4])
        elif lives == 1:
            print(stages[5])
        print("You losed one life.")
        print(f"You have {lives} left")
        
        if lives == 0:
            print(stages[6])
            print("Oops you lose!")
            break
    
        
    if "_" not in display:
        print("You win!")
        break
   # print(stages[lives])