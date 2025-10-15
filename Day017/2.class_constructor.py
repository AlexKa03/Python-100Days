class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

# Not user-friendly way
user_1 = User("001", "alex")
user_2 = User("002", "ivan")
user_3 = User("003", "emo")

print(user_1.followers)
