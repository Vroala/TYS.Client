from PyQt5.QtGui import *
from PyQt5 import QtWidgets, uic, QtCore 
import MyWindow
import sys
import pickle

class XWindow(QtWidgets.QMainWindow, MyWindow.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        self.initData()

        self.pushButton.clicked.connect(self.search)

        self.download.triggered.connect(self.saveData)
        self.folder.triggered.connect(self.openData)

        self.show()

    def search(self):
        keyword = self.lineEdit.text()
        resultData = self.sampleData[keyword]
        self.tableWidget.setRowCount(len(resultData))
        row = 0
        for item in resultData:
            self.tableWidget.setItem(row, 0, QTableWidgetItem(keyword))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item))
            row += 1

    def initData(self):
        self.sampleData = {
            'Python' : ['Fluent Python', 'Python Programming', 'Learning Python'],
            'go' : 'The Go Programming Language',
            'C#' : ['Inside C#', 'C# In Depth'],
            'C' : 'The C Programming Language'
        }

    def saveData(self):
        with open("test.data", "wb") as f:
            pickle.dump(self.sampleData, f)
        QtWidgets.QMessageBox.information(self, "저장", "데이터 저장됨")

    def openData(self):
        with open("test.data", "rb") as f:
            self.sampleData = pickle.load(f)
        QtWidgets.QMessageBox.information(self, "오픈", "데이터 로딩됨")

app = QtWidgets.QApplication(sys.argv)
xwin = XWindow()
sys.exit(app.exec_())
