import socket


UDP_IP = '127.0.0.1'
UDP_PORT = 4000
BUFFER_SIZE = 1024



def listen_forever():

   
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    s.bind(("", UDP_PORT))
    
    print("Server started at port "+str(UDP_PORT)+".")
    
    print("Accepting a file upload...")


    
    while True:
        
        data, ip = s.recvfrom(BUFFER_SIZE)
        
        if data.decode() == "-1":
          print("Upload successfully completed")
          break

        print( "Packet", data.decode())
       
        s.sendto("Receive Packet".encode(),ip)
        
        
    


    

listen_forever()
