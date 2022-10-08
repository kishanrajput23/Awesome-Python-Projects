# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 259)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(90, 180, 75, 23))
        self.login.setObjectName("login")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(190, 180, 75, 23))
        self.cancel.setObjectName("cancel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 80, 61, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 71, 16))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(303, 20, 20, 231))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.ip = QtWidgets.QLabel(self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(340, 80, 47, 16))
        self.ip.setObjectName("ip")
        self.login_2 = QtWidgets.QPushButton(self.centralwidget)
        self.login_2.setGeometry(QtCore.QRect(480, 180, 75, 23))
        self.login_2.setObjectName("login_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(460, 224, 47, 13))
        self.label_3.setObjectName("label_3")
        self.auth = QtWidgets.QLabel(self.centralwidget)
        self.auth.setGeometry(QtCore.QRect(500, 220, 81, 20))
        self.auth.setObjectName("auth")
        self.user = QtWidgets.QLineEdit(self.centralwidget)
        self.user.setGeometry(QtCore.QRect(130, 80, 113, 20))
        self.user.setObjectName("user")
        self.user_pwd = QtWidgets.QLineEdit(self.centralwidget)
        self.user_pwd.setGeometry(QtCore.QRect(130, 130, 113, 20))
        self.user_pwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.user_pwd.setObjectName("user_pwd")
        self.salt = QtWidgets.QTextEdit(self.centralwidget)
        self.salt.setGeometry(QtCore.QRect(400, 130, 131, 23))
        self.salt.setReadOnly(False)
        self.salt.setObjectName("salt")
        self.ip_2 = QtWidgets.QLabel(self.centralwidget)
        self.ip_2.setGeometry(QtCore.QRect(340, 130, 51, 16))
        self.ip_2.setObjectName("ip_2")
        self.ip_3 = QtWidgets.QLabel(self.centralwidget)
        self.ip_3.setGeometry(QtCore.QRect(400, 80, 131, 16))
        self.ip_3.setObjectName("ip_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.label.setText(_translate("MainWindow", "User Name:"))
        self.label_2.setText(_translate("MainWindow", "Password: "))
        self.ip.setText(_translate("MainWindow", "Client IP:"))
        self.login_2.setText(_translate("MainWindow", "Connect!"))
        self.label_3.setText(_translate("MainWindow", "Status: "))
        self.auth.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Unauthenticated</span></p></body></html>"))
        self.user.setPlaceholderText(_translate("MainWindow", "Username"))
        self.user_pwd.setPlaceholderText(_translate("MainWindow", "Password"))
        self.salt.setPlaceholderText(_translate("MainWindow", "Account ID"))
        self.ip_2.setText(_translate("MainWindow", "Auth Salt:"))
        self.ip_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaaa7f;\">&lt; Please Login&gt;</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

