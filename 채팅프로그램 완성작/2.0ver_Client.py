from PyQt5 import QtCore, QtGui, QtWidgets

from Form_1 import *
from Form_2 import *

import socket, threading, datetime, sys

th = []

HOST = 'localhost'	#호스트 주소
PORT = 20000		#포트 주소
ADDR = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)

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

class MyForm_1(QtWidgets.QDialog, Ui_Form):
	def __init__(self):
		QtWidgets.QDialog.__init__(self)
		self.setupUi(self)

	def sendClickSlot(self):
		sendMessage = '%s' % self.lineEdit.text()
		s.send(sendMessage.encode())
		myapp.close()

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

		myapp1 = MyForm_1()
		myapp1.show()

	except:
		try:
			myapp2 = MyForm_2()
			myapp2.show()

			sys.exit(app.exec_())
	
		except:
			pass
			s.close()

for t in th:
	t.join()