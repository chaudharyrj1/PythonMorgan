class  Evens:

    def __init__(self,limit):
        self.limit=limit
        self.val=0

    def __iter__(self):
        return self

    def next(self):
        if self.val>self.limit:
            raise StopIteration
        else:
            rval=self.val
            self.val+=2
            return rval

for i in Evens(11):
    print i
