class StringException(Exception):
    def __init__(self,msg="Enter String Arguments"):
        Exception.__init__(self,msg)

        
def demo(a):
    def inner(*args,**kwargs):
        print("This is inner")
        for i in args:
            if (type(i) != str):
                raise StringException
        for i in kwargs.values():
            if(type(i) != str):
                raise StringException
        a(*args,**kwargs) 
        print("Inner function finished execution")
        print()
    return inner
@demo 
def sayhi(name):
    print("Hi " + name)
@demo
def sayhello(name1,name2):
    print("Hello " + name1 + " " + name2)

    
try:
    sayhi("Flash")    
except StringException as e:
    print(e)
    print()
    
try:
    sayhello(2,"Wonder Woman")
except StringException as e:
    print(e)
    print()
    
try:
    sayhello(name1="Rooster",name2=10)
except StringException as e:
    print(e)