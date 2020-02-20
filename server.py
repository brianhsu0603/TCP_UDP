import socket 
from threading import Thread 
from socketserver import ThreadingMixIn 

class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        
 
   
TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

def listen_forever():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    threads = [] 
    

    while True:
        s.listen(4)
        print ("Multithreaded Python server : Waiting for connections from TCP clients...") 
        (conn, (ip,port)) = s.accept()
        print(f'Connection address:{ip,port}')
        data = conn.recv(BUFFER_SIZE)
        if not data: 
            print('No data received.')
            break
        print(f"received data:{data.decode()}")
        conn.send("pong".encode())
        newthread = ClientThread(ip,port) 
        newthread.start() 
        threads.append(newthread)
   
    for t in threads: 
     t.join() 



    conn.close()

listen_forever()