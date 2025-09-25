'''Filters: filter() is like a sieve—it lets only elements that satisfy the condition pass through.
Often used with lambda, but can also use normal functions.
'''

def even(a):
    return a%2==0

num=[1,2,3,4,5,6,7,8]

ans1=set(filter(even,num))
ans2=list(filter(even,num))
print(ans1)
print(ans2)