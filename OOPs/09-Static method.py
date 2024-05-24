#Create Class
class Phone:

    def powerOff(self): # Simple Function of class is takes ' self ' parameter is compulsory 
        print('Power off the Smartphone')

    @staticmethod    # -----> Decorators
    def powerOn():                           #Static Method does not need of takes any agrument && not ' self ' parameter is compulsory 
        print('Power On the Smartphone')

    
    
vivo =  Phone()  #create object

vivo.powerOff()  #non Static method 
vivo.powerOn()   #static method


   