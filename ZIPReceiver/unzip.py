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
		return tc
		
	def zipbz2(stri):
		sfile = "Bz2_uncompress_tempFile.bz2"
		desf = stri;
		t1 = time.time()
		cont = bz2.decompress(open(sfile,'rb').read())
		tc = time.time() - t1
		print("\nDecompression Time",tc)
		fh = open(desf,'wb')
		fh.write(cont)
		
		fh.close()
		return tc
