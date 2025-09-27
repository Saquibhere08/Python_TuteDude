'''
Iterator: An iterator in Python is an object that lets you go through items one by one.

iter() → makes an iterator.

next() → gives the next item.

list=[1,2,3,4,5]

for i in list:
    print(i)
'''
list=[1,2,3,4,5]
iteration=iter(list)
print(iteration.__next__())
print(next(iteration))