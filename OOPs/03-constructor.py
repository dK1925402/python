# In java if class ad method name is same then this method is known as Constructor
# but In python using '''  __init__ '''  keyword for create a Constructor

#Create class name is Myclass
class Myclass :

# create Constructor
    def __init__(self):
             print('It is Constructor , run automatically')

# create a method by same name of Class name is 'Myclass'
    def Myclass(self):
        print('It is Method ,') 


#Create an Object of Myclass name is 'obj'
obj = Myclass() #

#call to same class name method 
obj.Myclass()
