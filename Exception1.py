class NotLessThanException(Exception):
    pass

l=[1,2,3,4,5,6]
print l[5]
try:
    print l[6]
except Exception as e:
    print 'Exception: ',e
else:
    print "All Okay"
finally:
     print "It will always run"

try:
    a=input("enter digit less than 6")
    if a<6:
        print "You have entered ",a
    else:
        raise NotLessThanException,"Value is not less than 6"
except Exception as e:
    print "Exception: ",e