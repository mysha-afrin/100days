import random
number = [1, 2,3,4,5,6,7,8,9]
letters = ['a', 'b', 'c', 'd','e','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = ['!','@','#','$','%','&']
num = int(input("HOw many number do you want to take?"))
let = int(input("How many letters do you want?"))
sym = int(input("how many symbol do you want?"))
#easy level
password = ""
for char in range(1, num +1):
    

    password += str(random.choice(number))
for char in range(1, let + 1):
    password += str(random.choice(letters))
for char in range(1, sym + 1):
    password += str(random.choice(symbols))
print(password)