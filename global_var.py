n=1 #Global Variable outside an fn

def fn():
    global n #Global Variable inside an fn
    n=5 #Local variable
    print('in',n)

fn()

print('out',n)