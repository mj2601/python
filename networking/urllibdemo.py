import urllib.request

try:
	url = urllib.request.urlopen("https://www.python.org/")
	content = url.read()
	url.close()
except urlib.error.HTTPError:
	print ("The web page is not found")
	exit()

f = open('python.html','wb')
f.write(content)
f.close()