class User:
    def __init__(self, user_id, user_name, user_profession, user_country):
        self.user_id = user_id
        self.user_name = user_name
        self.user_profession = user_profession
        self.user_country = user_country
        self.follower = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.follower += 1


user_1 = User(1, "ARUN", "Java Programmer", "Canada")
user_2 = User(1, "VIMAL", "C++ Programmer", "INDIA")
user_1.follow(user_2)
