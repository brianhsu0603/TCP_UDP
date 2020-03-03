import socket 
from _thread import *
import threading 
from threading import Thread 

  



def threaded(conn): 
    
    while True: 
     
     data = conn.recv(1024) 

     if not data:

         break

     print(f"Received Data:{data.decode()}")
  
     conn.send("pong".encode()) 
  
   
   
  
def listen_forever(): 

 TCP_IP = '127.0.0.1'
 TCP_PORT = 5000

 
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 s.bind((TCP_IP, TCP_PORT))

 print("Server started at port " + str(TCP_PORT) + ".") 
    
 s.listen(5) 
   
 while True: 
  
    (conn, addr) = s.accept() 
    
    data = conn.recv(1024) 

    print(f"Connected Client:{data.decode()}")
    
    conn.send("Connected".encode())

    start_new_thread(threaded,(conn,))
 
 


listen_forever()

    
    


    
    

 

