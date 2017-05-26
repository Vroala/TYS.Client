from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from background import *

import socket, threading, datetime

th = []

HOST = 'localhost'	#호스트 주소
PORT = 50000		#포트 주소
ADDR = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

class MyForm(QtWidgets.QDialog, Ui_Dialog):
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		self.setupUi(self)

		#read = s.recv(1024)

		#if read == '-1':
		#	exit(0)

		#self.textEdit.append(read.decode())

		self.pushButton.clicked.connect(self.sendClickSlot)

	def sendClickSlot(self):
		#LineText 값을 가져오는 함수
		sendMessage = '%s' % self.lineEdit.text()
		s.send(sendMessage.encode())

if __name__ == "__main__":

	l = threading.Thread()
	th.append(l)
	l.start()

	try:
		app = QtWidgets.QApplication(sys.argv)
		myapp = MyForm()
		myapp.show()

		read = s.recv(1024)

		if read == '-1':
			exit(0)

		myapp.textEdit.append(read.decode())

		sys.exit(app.exec_())

	except:
		print('exit')
		pass
		exit(0)

for t in th:
	t.join()