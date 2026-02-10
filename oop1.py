
class Dog:

    def __init__(self,name,breed,hasFur):
         self.name =   name
         self.breed =  breed
         self.hasFur = hasFur


    def bark(self):
         print( self.name,"wooff! woof!")

    def locomotive(self):
        print(self.name,"Dog is walking")

dog1 = Dog("JJ","Rotweiler",True)
print(dog1.name, dog1.breed, dog1.hasFur)

dog2 = Dog("Tony","German shepherd",True)
print(dog2.name, dog2.breed, dog2.hasFur)

dog3 = Dog("Ann","SIberian husky",True)
print(dog3.name, dog3.breed, dog3.hasFur)

















