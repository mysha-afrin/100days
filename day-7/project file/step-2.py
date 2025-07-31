import random
word_list = ['soikot', 'camel', 'bungi', 'mango', 'banana']
chosen_word = random.choice(word_list)
print(chosen_word)
place_holder = ""
word_len = len(chosen_word)
for position in range(word_len):
    place_holder += "_"
    print(place_holder)
 
guess = input("Guess the word: ")
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)