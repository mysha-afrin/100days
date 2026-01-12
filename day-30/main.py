# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas


data = pandas.read_csv('day-30/nato_phonetic_alphabetes .csv')
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
try:
    word = input("Enter a word: ").upper()
    output_list = [phonetic_dict[letter] for letter in word]
    print(output_list)
except KeyError:
    word = input("please enter only letters from A to Z:").upper()
    output_list = [phonetic_dict[letter] for letter in word]
    print(output_list)
except KeyError as error_message:
    print(f"The letter {error_message} is not in the alphabet.")
