print("Welcome to the tip calculator!")
a = float(input("What is your ttal bill?"))
b = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
c = int(input("How many people to split the bill? "))
tip = ((a * b) / 100) / c
print(f"Each person should pay : {round(tip, 2)}")
