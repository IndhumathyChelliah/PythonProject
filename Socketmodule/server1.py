import socket

#default ipv4,tcp connection
s=socket.socket()
print ("Socket created Successfully")

s.bind(("localhost",9998))

s.listen(5)

print ("Waiting for Connection")

while True:
	c,addr=s.accept()
	name=c.recv(1024).decode()
	print ("Connected with",addr,name)

	c.send(bytes("Welcome to Python Programming","utf-8"))

	c.close()

