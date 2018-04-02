class Person:
    count=0
    def __init__(self,name):
        self.name=name
        Person.count+=1
    def __getattr__(self, item):
        print "attribute not found: ",item
        return 'unknown'

p=Person("rohit")
q=Person("john")

print Person.__dict__
print p.__dict__
print q.__dict__

print Person.count
print p.xx
print p.name
print p.count