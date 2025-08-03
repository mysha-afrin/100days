import random
word_list = ["algorithm", "elepant", "biologist", "happiness", "", "telegram", "notebook", "rainbow", "beautiful", "adventure", "stronger", "education", "Knowledge"]
lives = 6
chosen_word = random.choice(word_list)
print(chosen_word)
place_holder = ""
world_length = len(chosen_word)
for position in range(world_length):
    place_holder += "_"
print(place_holder)
stages = [  '''
      
     |    
     |      
     |      
     |       
     |      
     |
    _|__''','''
     _______
     |/     
     |     
     |     
     |     
     |     
     |
    _|___''',
    '''
     _______
     |/     |
     |     
     |     
     |      
     |     
     |
    _|___''' ,
    '''
     _______
     |/     |
     |     (_)
     |     
     |      
     |     
     |
    _|___ ''',
   '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___''' ,
    
    ''''
       _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
    _|___''']

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
    if guess not in chosen_word:
        lives -= 1
        print(lives)
        if lives == 0:
            print("You lose")
            print(lives)
            break
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
    elif lives == 0:
        print(stages[6])
    if "_" not in display:
        print("You win!")
        break
   # print(stages[lives])