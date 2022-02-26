import socket
import time as t
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = input("Введите IP адрес вашего устройства: ")
PORT = 12333
connection.connect((IP, PORT))
rd = connection.recv(1024)
print(rd.decode('utf8'))
while True:
	connection.send("И тебе привет!".encode('utf8'))
	t.sleep(2)
#connection.close()