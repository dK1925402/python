
''' In python “cls” implies that the method belongs to the class. 
Whereas, “self” implies that the method is related to an instance of the class'''


class Car :  #Create Class
    
    Car_Type = 'petrol'  #Delare the Car_Type variable its same for all the instance  

    def __init__(self ,car_name,topSpeed):  #constructor of a class contain to parameters 
        print ('Car name is : ',car_name, ' & top Speed : ',topSpeed)

    @classmethod  #decorators
    def classmethod (cls, type):     #this is class method is directly interact with class not like instance its change the real data of class
        cls.Car_Type= type  # in this (cls.Car_type  = Car.Car_Type)    
        

tesla = Car('tesla',500) #Create an instance of Car class 
nexon = Car('nexon',350) #Create an instance of Car class

print (Car.Car_Type) ## print the actual variable of class          Output : petrol

tesla.classmethod('Electric')  # change the class variable using classmethod 

print (Car.Car_Type) # after using the class method change the data of class type 




