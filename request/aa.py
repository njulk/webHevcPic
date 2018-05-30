#!/usr/bin/env python
#coding=utf8
'''
import httplib
import urllib
def sendPic(filename,dir):
	#x=open(dir,'rb')
	params=urllib.urlencode({'filename':filename},{"Content-Type":"image/jpeg",'image':open(dir,'rb')})
	headers={"Content-Type":"multipart/form-data","Accept": "text/plain"}
	client=httplib.HTTPConnection("localhost",8080,timeout=30)
	client.request("POST","/",params,headers)
	response=client.getresponse()
	#x.close()
	return


if __name__ == "__main__":
	sendPic("11.JPG","F:\\11.JPG")
'''
import requests
import json
def sendPic(filename,dir,size,model):
	data={"filename" : filename,
		  "cusize":size,
		  "modelname":model
		  }
	files={
		"image":open(dir,"rb")
	}
	x=requests.post("http://127.0.0.1:8080/",data,files=files)
	y=json.loads(x.text)
	#print y['data']
	return y['data']


#if __name__ == "__main__":
#	sendPic("11.JPG","F:\\11.JPG",32,"basketball")