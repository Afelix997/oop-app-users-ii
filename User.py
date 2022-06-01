class User:

    historical_posts= []

    def __init__(self,name,email,dl,age):
        self.name= name
        self.email= email
        self.dl= dl
        self.age= age
    def post(self,msg):
        self.historical_posts.append(f'{self.name} said: "{msg}"')
        return f'{self.name} said: "{msg}"'

angel= User('Angel','angel@goog.com',1234560,25)
terrance= User('Terrance','Terrance@goog.com',1234561,30)
zack= User('Zack','zack@goog.com',1234562,40)

angel.post('Hello World!')
terrance.post('1234!')
zack.post('Whoo!')

print(User.historical_posts)