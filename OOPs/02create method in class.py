
#Create an Employee class
class Employee:
      
      #define the printdetails method 
      def printdetails(self):
        return f'name is {self.name} and roll is {self.rollno}'



dhruv = Employee() #Create an Object of Employee class dhruv 
ayush = Employee() #Create an Object of Employee class ayush

#assign the variable 
dhruv.name = 'dhruv Kumar'
dhruv.rollno = 21

#assign the variable 
ayush.name = 'Ayush Kumar'
ayush.rollno = 22


#call to printdetails method of Employee class:
print(dhruv.printdetails())   #Output : name is dhruv Kumar and roll is 21
print(ayush.printdetails())   #Output : name is Ayush Kumar and roll is 22



