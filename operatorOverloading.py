'''Operator Overloading:Operator overloading in Python allows the same operator to have different
meanings depending on the data type or context, enabling custom objects to work with built-in operators like +, -, *, ==, 
and others. '''
'''
#method 1
a=1
b=2
print(a+b)

#method 2
print(int.__add__(a,b))
'''
class vegetables:
    def __init__(self,carrot,beans):
        self.carrot=carrot
        self.beans=beans

    def __add__(self,other): #operator overloading function
        carrot=self.carrot +other.carrot
        beans= self.beans + other.beans
        return vegetables(carrot,beans)
    
v1=vegetables(5,6)
v2=vegetables(7,8)
v3=v1+v2 #as we cannot directly add two classes so we need to define the above function

print(v3.beans)
print(v3.carrot)