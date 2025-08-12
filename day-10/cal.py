from art import logo
print(logo[0])
#calculate_again = input("Do you want to calculate again? (yes/no):").lower()
while calculate_again:
    calculate_again = input("Do you want to calculate again? (yes/no):").lower()
    if calculate_again == "yes" or calculate_again == "y":
        n1 = float(input("Enter first number: \n"))
        def add(n1, n2):
            return n1 + n2
        def subtract(n1, n2):
            return n1 - n2
        def multiple(n1, n2):
            return n1 * n2
        def divide(n1, n2):
            return n1 / n2
        calculate = input("What do you want to calculate ? (+, -, *, /)")
        if calculate == "+":
            print(add(n1, float(input("Enter second number:"))))
        elif calculate == "-":
            print(subtract(n1, float(input("Enter second number:"))))
        elif calculate == "*":
            print(multiple(n1, float(input("Enter second number"))))
        elif calculate == "/":
            print(divide(n1, float(input("Enter second number:"))))
        else:
            print("Invalid")
    elif calculate_again == "no" or calculate_again == "n":
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid input.")




