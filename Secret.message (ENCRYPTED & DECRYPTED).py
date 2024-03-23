# *******  Secret message python program for ENCRYPTED & DECRYPTED the message *******
# author = "Dhruv kumar"
# date : 23 March 2024
# secret message : "uyhk sab h ahar rak ih gnidoc sab rak htiab ihb ihba ay auh hcu?"



# IMPORT THE FILES
import random
import string
import sys

 
#GENERATE RANDOM STRING PROGRAM
def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length) )

#Call to function , generate 3 digit random string and stored this string into 'random_string' variable
random_string = generate_random_string(3)  # Change to your desired length


print('\n*******  Secret message python program  *******\n')

#CHOOSE - WHATS THE DO IN PROGRAM ON DECODE OR ENCODE THE MESSAGE 
choose = int(input('Choose the option :\n1.Encode the message \n2.Decode the message\n\nChoose :'))


#IF ENTER WRONG INPUT THEN EXIT THE PROGRAM 
if (choose != 1 and choose != 2):
    print('Please enter correct input')
    sys.exit()#THIS FN HELP IN FOR EXIT THE PROGRAM , USE THIS FN FOR IMPORT THE  """import sys"""
  

#INPUT MESSAGE FROM THE USER  
message = input("Enter your Message : ")

#FIND THE LENGTH OF THE MESSAGE 
length = len(message)



#IF CHOOSE 1 FOR --> Encode the message

if choose== 1 :

#IF THE LENGTH OF THE MESSAGE IN 1 OR 2 
   if(length<=2):

      if(length==1):
           print('Encoded message generate successfully :',message)
      
      else :
           first_char = message[0]
           last_char = message[-1]

           replaced_message = str(last_char + message[1:-1] + first_char)
           print('Encoded message generate successfully :',replaced_message)


#THE LENGTH OF THE MESSAGE MORE THAN 2  
   else :    
          first_char = message[0]
          last_char = message[-1]
         
        #  SUPPOSE ->string = 'Dhruv' 

         #REPLACE THE FIRST TO LAST CHARACTER & LAST CHARACTER TO FIRST CHARACTER , replace string = 'vhruD'
          replaced_message = str(last_char + message[1:-1] + first_char)
          
         #REVERSE THE REPLACE STRINT 'vhruD' ->  'Durhv'
          reverse_Message = replaced_message[::-1]

         #ADD RANDOM 3 DIGIT STRINT WITH REVERSE STRING 'Durhv' -> 'rtdDurhv'
          Encode_message = random_string +reverse_Message

          #PRINTED THE ENCRYPTED STRING
          print('Encoded message generate successfully :',Encode_message)

    
# CHOOSE 2 FOR --> Decode the message
elif(choose==2):
    
    #IF THE LENGTH OF THE MESSAGE IN 1 OR 2 
   if(length<=2):

         if(length==1):
           print('Encoded message generate successfully :',message)
         
         else :
           first_char = message[0]
           last_char = message[-1]
          
           replaced_message = str(last_char + message[1:-1] + first_char)
           print('Message decode successfully :',replaced_message)


#THE LENGTH OF THE MESSAGE MORE THAN 2 
   else:
        
        #SUPPOSE ENCODED string = 'rtdDurhv'
          
          #REMOVE FIRST THREE RANDOM STRING -> 'Durhv'
           Remove_random = str(message[3:])
          
          #REVERSE THE STRING -> 'vhruD'
           reverse_Message = str(Remove_random[::-1])
    
           first_char = reverse_Message[0]
           last_char = reverse_Message[-1]
          
          ##REPLACE THE FIRST TO LAST CHARACTER & LAST CHARACTER TO FIRST CHARACTER -> 'Dhruv'
           replaced_message = str(last_char + reverse_Message[1:-1] + first_char)

          #PRINTED THE DECRYPTED STRING 
           print('Message decode successfully : ',replaced_message)
     
     
     
