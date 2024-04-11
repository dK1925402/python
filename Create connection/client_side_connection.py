# ------  CLIENT Side Connection  ------

import socket #import for create connection and send data
import sys   #import for used only sys.exit()for exit from the program

#create function for close the connection
def closeconnection():
        print('[+] close the connection ...')#print  
        client_socket.send(b'close') #send to server 'close' for the connection
        client_socket.close()#close connection
        sys.exit()#exit from the program

#store the return data from socket.socket method in server_socket 
#socket.AF_INET = ipv4 (means which type of address)
#socket.SOCK_STREAM = TCP (means used which type of protocol)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ipv4 = '192.168.1.50' #enter the ip which laptop run in 'server_socket.py'
port_no = 15112 #Enter the any port_no.

#client_socket.connect for the connect the server
#used 'tuple' for store the ipv4 and port_no therefore its not run
client_socket.connect(('192.168.1.50',15112))

print('[+] Establish a connection Successfully...') 
    
print('[+] Enter "bye" for close the connection ...')#warn user for how to exit this from program

# use while True for chat the server with continuosly
while True :

      #For reply to server therefore store the input in reply
       reply = input('Enter your data : ') 

      #if condition is TRUE : input data is 'bye' then call closeconnection() fn  for close the connection
      #  #when if condition is false continue the program 
       if reply == 'bye' : closeconnection()  

      #Encode the reply data and send to the server
       client_socket.send(reply.encode()) 
       
       #store the recive data of the server in server_data and 1024 is a maximum size of data received from server
       server_data = client_socket.recv(1024)
       
       #if condition is TRUE : receive data from server is 'close' then call closeconnection() fn  for close the connection 
       #when if condition is false continue the program
       if server_data.decode() == 'close' : closeconnection()

      #decode the server reply and print them    
       print('Server reply -> ', server_data.decode())

      #  loop..
