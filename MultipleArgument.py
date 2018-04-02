def add(*args):
    print 'arguments: ',args
    x=0
    for n in args:
        x+=n
    return x

def display(**kwargs):
    print 'arguments: ',kwargs

c=add(2,3,5,3,2,4)

print c

display(x1=3,x2=6,x3=3,x4=32,x5=5,x6=2)
