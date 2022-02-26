import socket
import time as t
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "192.168.3.14"
PORT = 8090
connection.connect((IP, PORT))
rd = connection.recv(1024)
print(rd.decode('utf8'))
while True:
	send_sms = input("/")
	connection.send(send_sms.encode('utf8'))
#connection.close()
