'''
class Students:
    pass               ---> using pass keyword for define the empty class and method                   
'''

# Create a student class 
class Students:
    Colleage_name ='AIT'
    

#create an object of Students class
dhruv = Students()

#create extra variable of object(dhruv)
dhruv.rollno = 10622073
dhruv.sec = 'b'
dhruv.branch = 'CE'
dhruv.city= 'delhi'

print(dhruv.city)#print only the city of dhruv    : Output = delhi

print(dhruv.__dict__)#print all data of object in dictionary form     : Output =  {'rollno': 10622073, 'sec': 'b', 'branch': 'CE', 'city': 'delhi'}


print(Students.Colleage_name)      # : Output = AIT
print(dhruv.Colleage_name)         # : Output = AIT


#change the College_name variable for dhruv object 
dhruv.Colleage_name='dseu'     



