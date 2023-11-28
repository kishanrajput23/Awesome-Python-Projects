# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(327, 223)
        MainWindow.setMinimumSize(QtCore.QSize(327, 223))
        MainWindow.setMaximumSize(QtCore.QSize(327, 223))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 180, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 180, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 61, 16))
        self.label_2.setObjectName("label_2")
        self.un = QtWidgets.QLineEdit(self.centralwidget)
        self.un.setGeometry(QtCore.QRect(130, 50, 141, 20))
        self.un.setObjectName("un")
        self.un_pw = QtWidgets.QLineEdit(self.centralwidget)
        self.un_pw.setGeometry(QtCore.QRect(130, 100, 141, 20))
        self.un_pw.setEchoMode(QtWidgets.QLineEdit.Password)
        self.un_pw.setObjectName("un_pw")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "Cancel"))
        self.label.setText(_translate("MainWindow", "Username: "))
        self.label_2.setText(_translate("MainWindow", "Password: "))
        self.un.setPlaceholderText(_translate("MainWindow", "Username"))
        self.un_pw.setPlaceholderText(_translate("MainWindow", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

