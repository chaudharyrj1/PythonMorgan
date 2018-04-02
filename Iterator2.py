list=['a','b','c','d']
for i in list:
    print i

c=list.__iter__()
for i in range(4):
    print c.next()
  # print next(c)