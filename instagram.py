class Instagram:
    def __init__(self,username,name):
        self.usernmae = username
        self.name = name
        self.followers = 0
        self.following = 0

    def follow(self,user):
        self.following+=1
        user.followers+=1

user1 =Instagram("kavesh_raja","kavesh")
user2 =Instagram("shru","shruthi")
print(user1.usernmae,user1.name,user1.following,user1.followers)
print(user2.usernmae,user2.name,user2.following,user2.followers)
user1.follow(user2)
user2.follow(user1)
print(user1.usernmae,user1.name,user1.following,user1.followers)
print(user2.usernmae,user2.name,user2.following,user2.followers)
