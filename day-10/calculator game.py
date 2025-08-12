from art import logo
print(logo[0])


def add(n1, n2):
    return n1 + n2
    
def subtract(n1, n2):
    return n1 - n2
   
def multiple(n1, n2):
    return n1 * n2
    
def divide(n1, n2):
    return n1 / n2


calculate_dict = {"+" : add,
                   "-" : subtract,
                     "*" : multiple,
                       "/" : divide}

n1 = float(input("Enter first number: \n"))
n2 = float(input("Enter second number: \n"))
calculate = input("What do you want to calculate ? (+, -, *, /)")
if calculate in calculate_dict:
    result = calculate_dict[calculate](n1, n2)
    print(f"The result is : {result}")
    calculate_again = input("Do you want to calculate again? (yes/no):").lower()
    while calculate_again == "yes" or calculate_again == "y":
        n1 = float(input("Enter first number: \n"))
        n2 = float(input("Enter second number : \n"))
        calculate = input("What do you want to calculate ? (+, -, *, /)")
        if calculate in calculate_dict:
            result = calculate_dict[calculate](n1, n2)
            print(f"The result is : {result}")
            calculate_again = input("Do you want to calculate again? (yes/no):").lower()
        else:
            print("Invalid operation.")

print("Thank you for using the calculator!")