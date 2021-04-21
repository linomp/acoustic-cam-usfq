#!/usr/bin/python3           # This is client.py file

# center freq and width
# python client.py "../data/xml/16_mics_geom.xml" "../data/16_mics_samples.h5" "../data/test.bmp" 3000 3 0.3
# python client.py "../data/xml/3_mics_geom.xml" "../data/daq_test/acel_test_attr_2.h5" "../data/test.bmp" 2500 3 0.3

# given freqs
# python client.py "../data/xml/16_mics_geom.xml" "../data/16_mics_samples.h5" "../data/test.bmp" 2000 3000 0.3
# python client.py "../data/xml/3_mics_geom.xml" "../data/daq_test/acel_test_attr_2.h5" "../data/test.bmp" 2000 3000 0.3
# python client.py "../data/xml/16mg.xml" "../data/16ms.h5" "../data/test.bmp" 2000 3000 0.3

from os import sys
import socket

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def processArgsGivenFreqs(argv):
	micgeofile = argv[1]
	datafile = argv[2]
	imagefile = argv[3]
	lower_freq = argv[4].replace(",", ".") 
	higher_freq = argv[5].replace(",", ".")
	z_dist = argv[6].replace(",", ".")
	userThresh = argv[7].replace(",", ".")
	#userThresh = "2"
	sep = ','
	msg= sep.join([micgeofile, datafile, imagefile, lower_freq, higher_freq, z_dist, userThresh])	
	#print(msg)
	return msg


if len(sys.argv) > 2:
	#print(sys.argv)
	msg = processArgsGivenFreqs(sys.argv) 
elif len(sys.argv) == 2:
	msg ='exit'
else:
	eprint("missing args!")
	exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a socket object
host = socket.gethostname() # get local machine name    
port = 9999
s.connect((host, port))  # connection to hostname on the port.
s.send(msg.encode('utf-8')) 
msg = s.recv(1024).decode('utf-8')  # Receive no more than 1024 bytes        
if "error" in msg.lower():
  eprint (msg)
  sys.exit(1)  
else:
  print (msg)  
s.close()