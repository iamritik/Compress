import bz2, time,gzip
import os

class compressbz :
    @staticmethod
    def zip(fname):
        in_file = fname
        out_gz = "Bz2compression_tempFile.bz2"
        cl = 9
        sfile = in_file
        desf = out_gz
        ts = time.time()
        cont = bz2.compress(open(sfile,'rb').read(),cl)
        tc = time.time() - ts
        print("\nCompression time",tc)

        fh = open(desf,'wb')
        fh.write(cont)
        fh.close()
        return tc




