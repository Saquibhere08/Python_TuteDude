#write a generator program to get the squares of the numbers

def squares():
    n=1
    while n<=5:
        square = n**2
        yield square
        n=n+1
val=squares()
for i in val:
    print(i)