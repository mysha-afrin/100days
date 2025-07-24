print("Welcome to PYTHON PIZZA DELIVERY!")
size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
#The size of a pizza
if size == "s":
    bill = 250
if size == "m":
    bill = 350
elif size == "l":
    bill = 450
else:
    print("You typed wrong.")
#The pepperoni price

if pepperoni == "y":
    if size == "s":
        bill += 20
    else:
        bill += 35
#The extra cheese price
if extra_cheese == "y":
    bill += 25
print(f"Your final bill is: {bill} bdt.")
            
       