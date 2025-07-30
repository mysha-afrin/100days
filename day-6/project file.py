import random
word_list = ['Soikot', 'camel', 'bungi', 'mango', 'banana']
chosen_word = random.choice(word_list)
print(chosen_word)


#Make the user guess a word
guess = input(str("Guess a word:\n")).lower()


print(guess)


#Check if the guess word is right if right it will print write for each word
for letter in chosen_word:
    if chosen_word == guess:
        print("Right")
    else:
        print("Wrong")