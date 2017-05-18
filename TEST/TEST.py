# coding: utf-8

import sys
from PyQt5 import QtWidgets, QtGui, uic, QtCore 
from PyQt5.QtCore import pyqtSlot

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMinimumSize(QtCore.QSize(0, 200))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.slot_1st)
        self.pushButton_2.clicked.connect(self.slot_2nd)
        self.pushButton_3.clicked.connect(self.slot_3rd)
        self.lineEdit.textChanged['QString'].connect(self.label.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "여기에 출력됩니다."))
        self.pushButton.setText(_translate("Dialog", "첫번째 버튼"))
        self.pushButton_2.setText(_translate("Dialog", "두번째 버튼"))
        self.pushButton_3.setText(_translate("Dialog", "세번째 버튼"))

    @pyqtSlot()
    def slot_1st(self):
        self.label.setText("희태 혼밥")

    @pyqtSlot()
    def slot_2nd(self):
        self.label.setText("희태 투기장 갓승 3패")

    @pyqtSlot()
    def slot_3rd(self):
        self.label.setText("희태 등급전 방패병")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

