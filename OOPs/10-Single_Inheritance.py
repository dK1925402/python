import time
formatted_time = time.strftime("%H:%M", time.localtime())   #use this for find the curent time 
# print(formatted_time)              


#create watch class
class Watch :

    #constructor Show the current time automatically
    def __init__(self):
        print('Current time is : ',formatted_time)

     #for time change
    def time_change(self):
        print('Time Change successfully')

     #for timer 
    def timer(self):
        print('Start the Timer ......')   


# Create smart watch class also inherit with 'watch' class
class Smartwatch(Watch):

    # add calling fn
    def calling(self):
        print('Calling ......')

# add bluetooth feature
    def bluetooth(self):
        print('Pairing new device ......')    

# add StepCount feature
    def StepCount(self):
        print('Counting the Step')    

# Create noise instance of Smartwatch Class then its access watch and Smartwatch method
noise = Smartwatch()  

#then the constructor of watch class automatically call then create the instance of Smartwatch class because Smartwatch inherit the watch class

noise.time_change()  #access watch class method
noise.timer()        #access watch class method
noise.bluetooth()
noise.calling()
noise.StepCount()