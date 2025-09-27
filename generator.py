'''
A generator in Python is a special type of iterator that you create with a function using yield instead of return.
👉 It produces values one at a time, only when needed (lazy evaluation), saving memory.

'''
def fn():
    yield 1
    yield 2
    yield 3

values =fn()
print(values.__next__())

print(values.__next__())

print(values.__next__())

