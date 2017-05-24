# -*- coding: utf-8 -*-

import socket, threading, datetime

th = []

HOST = 'localhost'	#호스트 주소
PORT = 50000		#포트 주소
ADDR = (HOST, PORT)

def listen(s):
	global text

	while 1:
		read = s.recv(1024)

		if read == '-1':
			exit(0)

		print(data.decode(), '\n')

		data = input('메세지: ')

		if data == '-1':
			s.sendall('-1')

		s.sendall(data.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

try:
	l = threading.Thread(target=listen, args=(s,))
	th.append(l)
	l.start()

except:
	pass
	exit(0)

for t in th:
	t.join()