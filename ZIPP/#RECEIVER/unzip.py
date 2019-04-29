import bz2, time, gzip

class unzip:
	@staticmethod
	def zip(stri):
		sfile = "gzip_uncompress_tempFile.gzip"
		desf = stri;
		t1 = time.time()
		cont = gzip.decompress(open(sfile,'rb').read())
		tc = time.time() - t1
		print("\nDecompression Time",tc)
		fh = open(desf,'wb')
		fh.write(cont)
		
		fh.close()
