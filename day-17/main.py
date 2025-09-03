
class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
# pass is used as a placeholder for code that will be implemented later.
    #def __repr__(self):
      #  return f"User(username = {self.username}, id = {self.id}, password = {self.password})"
    def follow(self, user):
        user.followers += 1
        self.following += 1
#create user objects
user_1 = User("Angela", 1)
user_2 = User("Jack", 2)
user_1.follow(user_2)
#Print user objects
print(user_1.followers)
print(user_2.followers)