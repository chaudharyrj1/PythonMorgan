class a:
    def speak(self):
        print 'a'

class b(a):
   pass

class c(a):
    def speak(self):
        print 'c'

class d(b,c):
    pass

obj=d()
obj.speak()