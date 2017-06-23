from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from background import *

import socket, threading, datetime

th = []

HOST = '108.61.180.119'	#호스트 주소
PORT = 20000		#포트 주소
ADDR = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class MyForm(QtWidgets.QDialog, Ui_Dialog):
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		self.setupUi(self)

		s.connect(ADDR)

		self.pushButton.clicked.connect(self.sendClickSlot)
		l = threading.Thread(target=listen, args=(s, ))
		th.append(l)
		l.start()

	def sendClickSlot(self):
		sendMessage = '%s' % self.lineEdit.text()
		s.send(sendMessage.encode())
		self.lineEdit.setText('')

def listen(s):
	while 1:
		read = s.recv(1024)

		if read == '-1':
			exit(0)

		myapp.textEdit.append(read.decode())
		c = myapp.textEdit.textCursor();
		c.movePosition(QtGui.QTextCursor.End);
		myapp.textEdit.setTextCursor(c);

if __name__ == "__main__":

	try:
		app = QtWidgets.QApplication(sys.argv)
		myapp = MyForm()

		myapp.show()
		sys.exit(app.exec_())

	except:
		pass
		s.close()

	for t in th:
		t.join()