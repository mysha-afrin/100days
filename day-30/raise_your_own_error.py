height = float(input("Height:"))
weight = float(input("Weight:"))
if height <= 0 or height >=3:
    raise ValueError("Height must be greater than zero.")
bmi = weight / height ** 2
print(bmi)