#map
#map(function , iterable)

def squares(a):
    return a ** 2

num=[1,2,3,4,5]
ans=list(map(squares,num))
print(ans)

def squares1(b):
    return b ** 2

num1=[1,2,3,4,5]
res=list(filter(squares,num1))
print(res)
'''
The only difference between a map function and a filter function is that 
the map can return the squares of the above numbers but the filter cannot return
this is beacuase map allows to take the elements inside the list and apply function to that whereas the filter
creates the object but donot let any function to get applied to them.
'''