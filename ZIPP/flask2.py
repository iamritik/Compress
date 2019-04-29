from flask import Flask, request
from flask_cors import CORS, cross_origin
from flask_restful import Resource, Api
from json import dumps
from flask_jsonpify import jsonify
import json
from gzip_file import *;
from bz2_file import *;
from sender import *;
app = Flask(__name__)
api = Api(app)

CORS(app)

@app.route("/")
def hello():
           print("Hello")
           return jsonify("Hello")
                 
@app.route("/<fname>/<zip>")
def ReadFile(fname,zip):
	tc=""
	if(zip=="gzip"):
		print("\n\n\n\n",zip)
		tc = compress.zip(fname);
		sender.send(fname);
	else:
		print("\n\n\n\n",zip)
		tc = compressbz.zip(fname)
		sender.sendbz2(fname);
	ls = []
	ls.append(fname)
	ls.append(tc);
	data=fname+"||"+zip+"||"+str(float(tc))+"\n";
	record2(data);
	return jsonify(ls)

def record2(data):
	file=open("records.txt","a+");
	file.write(data);
	file.close();
	
	
if __name__ == '__main__':
     app.run(port=8000)
     app.debug=True
