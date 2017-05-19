# -*- coding: utf-8 -*-

import socket, threading, datetime

sem = thrading.Semphore()	#동시접속 통제
count = 0	#클라이언트 번호 매기기
th = []
conns = []

def to_client(conn, addr, count):
	cnt = count
	global conns

	for i in range(len(conns)):
		conns[i].sendall("%s에서, 유저 %d님이 접속하였습니다." % (addr[0], cnt))

	print("%s에서, 유저 %d님이 접속하였습니다." % (addr[0], cnt))
	conn.sendall("서버에 접속하였습니다. \n당신은 유저 %d입니다." % (cnt))

	try:
		while 1:
			read = conn.recv(1024)

			if read == '-1':
				conn.sendall('-1')
				exit(0)

			read = "유저 %d : %S" % (cnt, read)
			print(read)

			for i in range(len(conns)):
				conns[i].sendall(read)

	except:
		print("유저 %d 님이 나가셨습니다." % (cnt))
		conns.remove(conn)

		for i in range(len(conns)):
			conns[i].sendall("유저 %d 님이 나가셨습니다." % (cnt))

		exit(0)

s = socket.socks