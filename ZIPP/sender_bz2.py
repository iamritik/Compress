from socket import *;
import socket# Import socket module
import os
import codecs
import bz2, time,gzip


class sender :
  @staticmethod
  def send(fname):
   port = 1300                    # Reserve a port for your service.
   s = socket.socket()
   print("File Name:",fname);                              # Create a socket object
   host = socket.gethostname()  # Get local machine name
   print("Server's Name:",host)
   s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
   s.bind((host,port))            # Bind to the port
   s.listen(1)                     # Now wait for client connection.
   
   while True:
    conn, addr = s.accept()     # Establish connection with client.
    print ('\n\n\nGot connection from', addr)
    conn.send(fname.encode('utf-8'));
    
    f = open('Bz2compression_tempFile.bz2','rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       #print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    os.remove("'Bz2compression_tempFile.bz2")
    conn.close()

if __name__ == '__main__':
     sender.send();
