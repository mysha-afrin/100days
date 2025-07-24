age = int(input("Enter your age: "))
height = int(input("Enter you height in ft:"))
bill = 0
if height >= 5 and height <= 7:
    print("You are eligible to ride")
    if age <= 8:
        bill = 100
        print("You ticket price 100bdt")
    elif age <= 12 and age > 8:
        print("your ticket price is 120 bdt.")
        bill = 120
    else:
        print("Your ticket price is 150 bdt.")
        bill = 150
    a = input('Do you want to taka a photo?"y" for yes and "n" for no.')
    if a == 'y':
        bill += 3
        print(f"You total ticket prize is {bill} bdt.")
    else:
        print(f"You total ticket prize is {bill} bdt.")
else:
    print("You are not eligible to ride")
