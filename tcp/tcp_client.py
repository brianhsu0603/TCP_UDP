
import socket
import sys
import time
import threading
from threading import Thread 



TCP_IP = '127.0.0.1'
TCP_PORT = 5000
MESSAGE = "ping"


id = sys.argv[1]

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

c.connect((TCP_IP, TCP_PORT))

c.send(f"{id}".encode())

data = c.recv(1024) 


for x in range(0,int(sys.argv[3])):
      
    c.send(f"{id}:{MESSAGE}".encode())
    
    print(f"Sending data:{MESSAGE}")
    
    data = c.recv(1024)
    
    print("Received data:", data.decode())
     
    
    time.sleep(int(sys.argv[2]))
  
     




    
 

     




