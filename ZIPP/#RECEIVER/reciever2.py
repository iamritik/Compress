import socket ;
from unzip import *;
import os

s = socket.socket()             # Create a socket object
host = "PC415499"
print ("Server's name:",host);				# Get local machine name
port = 1300             # Reserve a port for your service

s.connect((host, port))
i=0
data = s.recv(1024)
stri=data.decode('utf-8');
print("File to be received:",stri); 
with open('gzip_uncompress_tempFile.gzip', 'wb') as f:
        print('\nFile transmitting...')
        while True:
                print('\nreceiving data...')
                data = s.recv(1024)
                if not data:
                        break
                f.write(data)
f.close()
print('\nSuccessfully got the file')

s.close()
print('\nConnection closed')
print("File ",stri,"successfully received!");
unzip.zip(stri)

os.remove("gzip_uncompress_tempFile.gzip")

