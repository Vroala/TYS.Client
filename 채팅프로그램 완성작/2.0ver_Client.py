# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

from Form_1 import *
from Form_2 import *

import socket, threading, datetime, sys

th = []
flag = 0

HOST = '108.61.180.119'	#호스트 주소
PORT = 20000		#포트 주소
ADDR = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

def listen(s):
	while 1:
		read = s.recv(1024)

		if read == '-1':
			exit(0)

		myapp2.textEdit.append(read.decode())
		c = myapp2.textEdit.textCursor();
		c.movePosition(QtGui.QTextCursor.End);
		myapp2.textEdit.setTextCursor(c);

class MyForm_1(QtWidgets.QDialog, Ui_Form):
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		self.setupUi(self)

	def sendClickSlot(self):
		global flag

		sendMessage = '%s' % self.lineEdit.text()
		print(len(sendMessage.encode('cp949')))
		
		if len(sendMessage.encode('cp949')) > 0 and len(sendMessage.encode('cp949')) < 17:
			s.send(sendMessage.encode())
			flag = 1
			myapp1.close()
		else:
			msg = QtWidgets.QMessageBox.warning(self, '유저 이름 오류!', '한글 이름은 8자리\n영어 이름은 16자리 까지 가능합니다.')


class MyForm_2(QtWidgets.QDialog, Ui_Dialog):
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		self.setupUi(self)

		self.pushButton.clicked.connect(self.sendClickSlot)
		l = threading.Thread(target=listen, args=(s, ))
		th.append(l)
		l.start()

	def sendClickSlot(self):
		sendMessage = '%s' % self.lineEdit.text()
		s.send(sendMessage.encode())
		self.lineEdit.setText('')

if __name__ == "__main__":

	try:

		app = QtWidgets.QApplication(sys.argv)

		myapp1 = MyForm_1()
		myapp1.show()

		app.exec_()

		if flag == 1:
			myapp2 = MyForm_2()
			myapp2.show()

			sys.exit(app.exec_())

	except:
		pass
		s.close()


for t in th:
	t.join()