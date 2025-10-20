def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
print(add(5, 10, 15, 20))



def calcultate(n, **kwargs):
    for key, value in kwargs.items():
        print(f" kwargs : {kwargs}")
        n *= kwargs["multiply"]
        n += kwargs["add"]
        print(n)

calcultate(2,add=5, multiply=10)