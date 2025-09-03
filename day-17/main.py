
class User:
    def __init__(self, username, id, password):
        self.username = username
        self.id = id
        self.username = username
        self.password = password
# pass is used as a placeholder for code that will be implemented later.
    def __repr__(self):
        return f"User(username = {self.username}, id = {self.id}, password = {self.password})"
    
#create user objects
user_1 = User("Angela", 1, "password123")
user_2 = User("Jack", 2, "qwerty")
#Print user objects
print(user_1)
print(user_2)