# ------  SERVER Side Connection  ------

import socket  #import for create connection and send data  
import sys  #import for used only sys.exit()for exit from the program

#create function for close the connection
def closeconnection():
   print('[+] close the connection ...')#print
   conn.send(b'close') #send to client 'close' for the connection
   conn.close()#close connection
   sys.exit()#exit from the program

#store the return data from socket.socket method in server_socket 
#socket.AF_INET = ipv4 (means which type of address)
#socket.SOCK_STREAM = TCP (means used which type of protocol)
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


ipv4 = '192.168.1.50' #enter the ip which laptop run in 'server_socket.py'
port_no = 15112 #Enter the any port_no.

#bind server_socket with ipv4 and port no.
#used 'tuple' for store the ipv4 and port_no therefore its not run
server_socket.bind((ipv4,port_no))

#create listner this listner listen the 10 client in a one time also increase this 
server_socket.listen(10)
print('[+] Establish a connection ...')

#server_socket.accept return the two values therefore used two variable for store the return data 
#conn store the connection data 
# addr store the socket(ip and port) of the client
conn , addr = server_socket.accept()

# print the socket(ip and port) of the client
print('[+] Connected with client Successfully .....',format(addr))

print('[+] Enter "bye" for close the connection ...')#warn user for how to exit this from program
  
# use while True for chat the client with continuosly
while True :

     data = conn.recv(1024) #store the recive data of the client 1024 is a maximum bitssize of data received from server
     client_data = data.decode()#decode the add the and store in client client_data 
     
     #if condition is TRUE : receive data from client is 'close' then call closeconnection() fn  for close the connection 
     #when if condition is false continue the program
     if client_data == 'close': closeconnection()
      
       
     print('client reply -> ',client_data)#print the client data 
     
     #For reply to client therefore store the input in server_reply
     server_reply = input('Enter your data : ')

     #if condition is TRUE : input data is 'bye' then call closeconnection() fn  for close the connection
     #  #when if condition is false continue the program 
     if server_reply == 'bye' : closeconnection()
   
     #send the data store input in server_reply to the client
     conn.send(server_reply.encode())

   #   loop ...
  
