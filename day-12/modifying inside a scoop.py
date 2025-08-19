enemies = 1

def increase_enemies():
    global enemies   #using global allows us to modify the global variable
    enemies += 1
    print(f"Enemies increased to {enemies}")

increase_enemies()
print(f"Current number of enemies outside function: {enemies}")

'''Modifying global scoop is not encouraged. Instead of modifying global scoop we can use return statement.
 The block of code under thos will show it .'''

def increase_enemies_1(enemies):
    print(f"Enemies inside function : {enemies}")
    return enemies + 1
enemies = increase_enemies_1(enemies)
print(f"Enemies outside function : {enemies}")