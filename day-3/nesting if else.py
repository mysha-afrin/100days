
age = int(input("Enter your age: "))
height = int(input("Enter you height in ft:"))

if height >= 5 and height <= 7:
    print("You are eligible to ride")
    if age <= 8:
        print("You ticket price 100bdt")
    elif age <= 12 and age > 8:
        print("your ticket price is 120 bdt.")
    else:
        print("Your ticket price is 150 bdt.")
else:
    print("You are not eligible to ride")
