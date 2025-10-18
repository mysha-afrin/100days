def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
print(add(5, 10, 15, 20))