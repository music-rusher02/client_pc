import socket
import time as t
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = input("Введите IP адрес вашего устройства: ")
port = input("Введите PORT вашего устройства: ")
PORT = int(port)
connection.connect((IP, PORT))
rd = connection.recv(1024)
print(rd.decode('utf8'))
while True:
	send_sms = input("/")
	connection.send(send_sms.encode('utf8'))
#connection.close()
