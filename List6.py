#List Comprehension

#Method 1
x=[]

for i in range(11):
    z=i**2
    x.append(z)
print(x)

#Method 2
x=[i**2 for i in range(11)]
print(x)