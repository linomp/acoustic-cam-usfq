#!/usr/bin/python3           # This is server.py file
import socket  
from beamforming import *
from pylab import show

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object
host = socket.gethostname() # get local machine name
port = 9999 
serversocket.bind((host, port))  # bind to the port
serversocket.listen(5) # queue up to 5 requests    

print("Serving on %d" % port)
clientsocket,addr = serversocket.accept()
print("dummy connection! " + str(addr))
clientsocket.close()
while True:  
  clientsocket,addr = serversocket.accept()  # establish a connection
  #msg = 'Processing request...'+ "\r\n"
  #clientsocket.send(msg.encode('utf-8'))
  args = clientsocket.recv(1024).decode('utf-8').split(',')
  if(args[0]=='exit'):
    print('Closing server...')
    break
  #print(args)
  try: 
    doBeamformingGivenFreqs(args) # forward arguments to beamforming module
    clientsocket.send(('Success! (Close plot to continue).'+ "\r\n").encode('utf-8'))
    show()
    clientsocket.close() 
  except Exception as e:
    clientsocket.send(('Error: ' + str(e)).encode('utf-8'))
    clientsocket.close()
  

