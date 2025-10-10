#Inheritance

class name: #base class
    x=0
    name=" "

    def __init__(self,z):
        self.name=z
        print("hi",z)

class football_fans(name): #Sub-class
    points=0

    def pts(self):
        print(self.name,"scores")

n=name("Saquib")

f=football_fans("JIM")
f.pts()
