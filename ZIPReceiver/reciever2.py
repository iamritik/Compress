import socket ;
from unzip import *;
import os

class receive:
	def receive():
		s = socket.socket()             # Create a socket object
		host = "PC415499"
		print ("Server's name:",host);				# Get local machine name
		port = 1300             # Reserve a port for your service

		s.connect((host, port))
		i=0
		data = s.recv(1024)
		reccc=data.decode('utf-8');
		print("\n\n\n\n\n\n",reccc)
		stri=reccc.split(':')[0]
		zippp=reccc.split(':')[1]
		print("File to be received:",stri); 
		
		if(zippp=="gzip"):
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
			tc = unzip.zip(stri)
			data=stri+"||"+"gzip"+"||"+str(float(tc))+"\n";
			record2(data);

			os.remove("gzip_uncompress_tempFile.gzip")
		if(zippp=="bz2"):
			with open('bz2_uncompress_tempFile.bz2', 'wb') as f:
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
			tc = unzip.zipbz2(stri)

			os.remove("Bz2_uncompress_tempFile.bz2")
			data=stri+"||"+"bz2"+"||"+str(float(tc))+"\n";
			record2(data);
		
		return stri,tc,zippp;

def record2(data):
	file=open("records.txt","a+");
	file.write(data);
	file.close();

if __name__ == '__main__':
     receive.receive();