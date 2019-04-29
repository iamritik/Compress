import bz2, time,gzip
import os

class compress :
    @staticmethod
    def zip(fname):
        in_file = fname
        out_gz = "Gzipcompression_tempFile.gz"
        cl = 9
        sfile = in_file
        desf = out_gz
        ts = time.time()
        cont = gzip.compress(open(sfile,'rb').read(),cl)
        tc = time.time() - ts
        print("\nCompression time",tc)

        fh = open(desf,'wb')
        fh.write(cont)
        fh.close()
        return tc





