
'''
pip3 install func_timeout 
'''

import socket
from func_timeout import func_timeout

UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024

def getConnection():
    
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendMessage(s=None):
    
    wait_time = 0.0000015
    
    id = 1

  
 
    if not s:
        s = getConnection() #socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Connected to the server.")
        print("Starting a file upload...")
        server_ack = True
        with open('upload.txt','r') as file:
            message = file.readline() #Read first line in file 
            message_state = [message,0] #(message, re-connect count)
            while message:
                if message != message_state[0]:
                    message_state = [message,0] #Reset re-connect count for a new message
               
                
                s.sendto(str(message).encode(), (UDP_IP, UDP_PORT))
                
               
                try:
                  data, ip = func_timeout(wait_time,s.recvfrom,(BUFFER_SIZE,))
                  print ("Receive ack(" + str(id) + ") from the server")
                  id += 1
                  message = file.readline() #Read next line if server ack received

                except:
                    print("Packet loss, resend it")
                    message_state[1] += 1  #Decrement number of re-connects remaining
                    if message_state[1] < 100:
                        s = getConnection() #Since UDP is stateless, we must re-connect to the server
                    else:
                        print("resent it 100 times still fails")
                        exit()
                 
       
                
    
    print("File upload successfully completed.")
    s.sendto(str(-1).encode(), (UDP_IP, UDP_PORT))
 

    
    
sendMessage()