#wifi class
class Wifi :
    def wifion(self):
        print('wifi on .....')

#Radio class
class Radio:
    def radio(self):
        print('FM radio starting ......')

#Phone class
class Phone:
    def Call(self):
        print('Calling to Draken ....')

#Torch class
class Torch :
    def torch_on(self):
        print('Flash ......')


#Inherit Multiple classes in SmartPhone class is Known as "Multiple inheritance"
class SmartPhone(Wifi,Radio,Phone,Torch):

    def Ram_Rom(self):
        print('12GB RAM && 1TB ROM')

#Create instance of Smartphone class
oppo = SmartPhone()

#Calling to functions
oppo.Ram_Rom()
oppo.wifion()
oppo.Call()
oppo.radio()
oppo.torch_on()





