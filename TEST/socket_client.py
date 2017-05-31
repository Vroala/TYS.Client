# -*- coding: utf-8 -*-

from socket import *

HOST = '108.61.180.119'
PORT = 20000
ADDR = (HOST, PORT)

serSocket = socket(AF_INET, SOCK_STREAM)
serSocket.connect(ADDR)

while True:
	data = input('> ')

	if not data :
		break

	serSocket.send(data.encode())
	data = serSocket.recv(1024)

	if not data:
		break

	print('Received', data.decode())

serSocket.close()