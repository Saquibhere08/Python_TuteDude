#Constructors and Destructors
'''
Constructor (__init__) → Runs when object is created → Initializes.

Destructor (__del__) → Runs when object is destroyed → Cleans up. 

'''

class const_dest:
    x=0

    def __init__(self,color,type):
        self.color=color
        self.type=type
        print("Constructed")

    def __del__(self):
        print("Destructed")

cd=const_dest("BLack","SUV")
print(cd.color)
print(cd.type)

cd_1=const_dest("Red","Sedan")
print(cd_1.color)
print(cd_1.type)