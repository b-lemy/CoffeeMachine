# Working with constructors

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0
        print('the constructor')

    def follow(self, user):
        user.follower += 1
        self.following += 1


user_1 = User('005', 'Brian')
user_2 = User('001', 'Lema')

# username is an attribute
user_1.username = 'Brian'

user_1.follow(user_2)


print(user_2.follower)
print(user_1.follower)
print(user_2.following)
print(user_1.following)