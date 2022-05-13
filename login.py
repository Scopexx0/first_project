class User:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    base = dict()

    def create(self):
        while self.user in self.base:
            return "already exist"
        else:
            self.base[self.user]= self.password
            return f"new user: {self.user}"

    def login(self, user, password):
        if user == self.user:    
            if password == self.base[user]:
                return "Login succesful!"
            else:
                return "incorrect psw"
        else:
            return "incorrect name"


#Test with random users(you can test it with your own cases)

# p1 = User("scopexX", 123)
# print(p1.create())
# print(User.base)
# print(p1.login('scopexX', 123))

# print('*****************')

# p2 = User("steve", 111)
# print(p2.create())
# print(User.base)
# print(p2.login("steve",111))

# print('*****************')

# p3 = User("jhon", 12345)
# print(p3.create())
# print(User.base)
# print(p3.login("jhon",12345))

# print('*****************')

# p4 = User("talon", 11133)
# print(p4.create())
# print(User.base)
# print(p4.login("talon",11133))