try:
    age = int(input("Enter your age : "))
except ValueError:
    print("Please enter a valid intizer for age.")
    age = int(input("Enter your age again:"))
if age > 18:
    print(f"You can drive at the age of {age}")