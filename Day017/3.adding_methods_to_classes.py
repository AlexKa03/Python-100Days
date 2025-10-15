class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1

# Not user-friendly way
user_1 = User("001", "alex")
user_2 = User("002", "ivan")
user_3 = User("003", "emo")

user_1.follow(user_2)

print(f"{user_1.username} follows {user_1.following} users and has {user_1.followers} followers.")
print(f"{user_2.username} follows {user_2.following} users and has {user_2.followers} followers.")
print(f"{user_3.username} follows {user_3.following} users and has {user_3.followers} followers.")
