import web
import json
urls = (
	'/', 'index'
)


class index:
	def GET(self):
		return "Hello, world!"
	def POST(self):
		x=web.input()
		if 'image' and 'filename' in x:
			fout = open('E:\\' + x.filename, 'wb')
			fout.write(x.image)
			fout.close()
		if 'filename' in x:
			print x.filename
		if 'cusize' in x:
			print x.cusize
		if 'modelname' in x:
			print x.modelname
		return json.dumps({"data":2})

#class intraPredict:
#	def getDir(self,modelname,picname,size):





if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()