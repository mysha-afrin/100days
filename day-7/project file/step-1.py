import random
word_list = ["banana", "apple", "reach", "terminal", "overtime"]
chosen_word = random.choice(word_list)#chooses a word randomly.
print(chosen_word)
guess = input("Guess a word :")
print(guess)
place_holder = "_"
word = (place_holder * len(chosen_word))
print(word)
for word in chosen_word:
    if word in guess:
        print("Right")
    else:
        print("Wrong")