def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
print(add(5, 10, 15, 20))



class car:
    def __init__ (self, **kwargs):
        print(kwargs)
        n += kwargs["add"]
        n *= kwargs["multiply"]
        print(n)
car(2, add = 3, multiply = 5)