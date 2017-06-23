# -*- coding: utf-8 -*-

import socket, threading, datetime

sem = threading.Semaphore()	#동시접속 통제
count = 0	#클라이언트 번호 매기기
th = []
conns = []

HOST = ''	#호스트 주소
PORT = 20000		#포트 주소
ADDR = (HOST, PORT)

def to_client(conn, addr, count):
	cnt = count
	global conns

	for i in range(len(conns)):
		sendMessage = "시스템메세지 : %s에서, 유저 %d님이 접속하였습니다." % (addr[0], cnt)
		conns[i].send(sendMessage.encode())

	print("시스템메세지 : %s에서, 유저 %d님이 접속하였습니다." % (addr[0], cnt))
	sendMessage = "시스템메세지 : 서버에 접속하였습니다. \n시스템메세지 : 당신은 유저 %d입니다." % (cnt)
	conn.send(sendMessage.encode())

	try:
		while 1:
			read = conn.recv(1024)	#메세지 받기

			read = read.decode()

			if read == '-1':
				conn.send('-1')
				exit(0)

			read = '유저 %d번님 : %s' % (cnt, read)

			D=datetime.datetime.today()
			print('[%s] %s' % (D.ctime(), read))

			for i in range(len(conns)):		#전체 유저를 i에 각각 저장
				conns[i].send(read.encode())		#유저 전체에게 메세지 보내기

	except:
		print("유저 %d번님이 나가셨습니다." % (cnt))	#유저의 접속이 끝겼을때 메세지 표시
		conns.remove(conn)						#접속이 끊긴 유저를 지우기

		for i in range(len(conns)):				#나머지 전체 유저를 i에 각각 저장
			sendMessage = "유저 %d번님이 나가셨습니다." % (cnt)
			conns[i].send(sendMessage.encode())	#나머지 유저 전체에게 메세지 전송

		exit(0)									#연결 종료

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDR)
s.listen(1)

while 1:	#반복문을 이용해 여려명의 클라이언트를 받음(쓰레드의 기능 활용)
	conn, addr = s.accept()	#연결된 클라이언트 정보를 입력
	conns.append(conn)		#연결목록이 저장된 곳에 지금 연결된 클라이언트를 추가
	sem.acquire(); count += 1; sem.release()	#Semaphore의 사용
	client = threading.Thread(target=to_client, args=(conn, addr, count))	#쓰레드를 이용해 클라이언트 소켓 생성
	client.start()	#클라이언트와 연결
	th.append(client);	#쓰레드에 클라이언트 추가

for t in th:
	t.join()	#접속이 끊길때 까지 유지