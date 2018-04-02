a=input("Enter the limit upto which you want to see even numbers")
for n in range(a):
    l=range(a)
    l=filter(lambda a:a%2==0,l)
for n in l:
    print n