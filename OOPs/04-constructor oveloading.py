# In Python, constructor overloading, as it's understood in some other programming languages like Java,
#  isn't directly supported due to Python's dynamic nature.

'''' class Myclass :
    def __init__(self):
        print('Hello World')
In Python, constructor overloading, as it's understood in some other programming languages like Java,
#  isn't directly supported due to Python's dynamic nature.
    def __init__(self,name):
        print ('hello ', self.name)

    def __init__(self,name1,name2):
        print ('hello ',self.name1 ,' & ',self.name2) 
'''

# In python we can do constructor overloading like this   

class Myclass:
    def __init__(self, name1=None, name2=None):

        if name1 is not None and name2 is not None:
            print('hello', name1, '&', name2)

        elif name1 is not None:
            print('hello', name1)

        else:
            print('Hello World')

# Now you can create instances like this:
obj1 = Myclass()  # This will print 'Hello World'
obj2 = Myclass('Dhruv')  # This will print 'hello Dhruv'
obj3 = Myclass('Dhruv', 'Deepanshu')  # This will print 'hello Dhruv & Deepanshu'

