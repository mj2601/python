import socket
host = 'localhost'
port = 6767

s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))

s.listen(1) 
print("server listening on port:",port)

c,addr = s.accept()

fileName = c.recv(1024)

try:
	f = open(fileName,'rb')
	content = f.read()
	c.send(content)
	f.close()
except FileNotFoundError:
	c.send(b"File doesa not exist")

c.close()