# -*- coding: utf-8 -*-

from socket import *

HOST = ''
PORT = 20000
ADDR = (HOST, PORT)

serSocket = socket(AF_INET, SOCK_STREAM)
serSocket.bind(ADDR)
serSocket.listen(1)

while True:
	print ('Waiting For Connection...')
	cliConn, cliAddr = serSocket.accept()
	print('Connected by', cliAddr)

	while True:
		data = cliConn.recv(1024)
		if not data:
			break
		cliConn.send(data)

	cliConn.close()

serSocket.close()