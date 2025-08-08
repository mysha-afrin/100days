programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "function": "A piece of code that you can easily call over and over again."}


print(programming_dictionary["Bug"])


#Adding new items to the dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
print(programming_dictionary)


#editing a dictionary item
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

#looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])