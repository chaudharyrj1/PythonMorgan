class Person:
    count=0
    def __init__(self,name):
        self.name=name
        Person.count+=1
    def __str__(self):
        return "Person Name:{}".format(self.name)
        #detail="Person Name:["+self.name+"]"      return detail

p=Person("Amit")
print p