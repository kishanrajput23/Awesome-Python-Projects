from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_MainWindow
import sys

class MyFirstGuiProgram(Ui_MainWindow):
    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)

        # Connect "add" button with a custom function (addInputTextToListbox)
        self.pushButton.clicked.connect(self.retrieve)
        self.pushButton_2.clicked.connect(self.exit)

    def exit(self):
        sys.exit(app.exec_())

    def retrieve(self):
        un = self.un.text()
        pw = self.un_pw.text()
        u=open('user.dat','w')
        p=open('pwd.dat','w')
        u.write(un)
        p.write(pw)
        u.close()
        p.close()
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()

    prog = MyFirstGuiProgram(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())
