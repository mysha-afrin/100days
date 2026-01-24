import random
print("imported")
with open("day-32/birthday.txt", "r") as file:
    print("opening file")
    quote_lines = file.readlines()
   # print(quote_lines)
if not quote_lines:
    print("file is empty")
else:
    random_quote = random.choice(quote_lines)
    print(random_quote)
print('randomly_choosen')
