def add(i,j):
    return i+j

def call(i,j):
    return add(i,j)

def pas(i,j,fn):
    return fn(i,j)

#function within another function
res=pas(1,99,call)
print(res)

