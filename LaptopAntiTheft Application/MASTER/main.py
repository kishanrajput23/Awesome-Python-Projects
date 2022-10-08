import sys
import MySQLdb
import _thread
import os
import socket
from PyQt5 import QtWidgets
import db

from login_ui import Ui_MainWindow


class Mainclass(Ui_MainWindow):
    def __init__(self,MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        self.usr=None
        self.client_identifier=None
        self.auth_stat = "Not_Authenticated"
        self.login.clicked.connect(self.login_initiator)
        self.cancel.clicked.connect(self.exit)
        self.login_2.clicked.connect(self.connect_thread)
        self.auth_stat="No"

    def connect_thread(self):
        _thread.start_new_thread(self.connect, ())

    def login_initiator(self):
        _thread.start_new_thread(self.login1, ())

    def login1(self):

        # auth99 is to check your authentication status
        # if auth99 = 1 --> login success or otherwise failed
        if self.auth_stat is "No":
            self.usr = self.user.text()
            pwd = self.user_pwd.text()
            print(self.auth_stat)
            auth99 = 1
            db = MySQLdb.connect("localhost", "root", "toor", "credentials")
            print("conn")
            cursor = db.cursor()
            auth99 = cursor.execute("SELECT * FROM MASTER WHERE USER = '" + self.usr + "' AND PASS = '" + pwd + "'")
            print(auth99)
            if auth99 is 0:
                self.auth_stat="No"
                os.system('login_ack_fal.py')
                self.auth.setText("<html><head></head><body><p style=\"color:#ff0000;\">Unauthenticated</p></body></html>")
                print(self.auth_stat)
            else:
                # cursor.execute("SELECT * FROM MASTER WHERE USERNAME = '" + usr + "' AND PASSWORD = '" + pwd + "'")
                self.auth_stat="Yes"
                os.system('login_ack_scs.py')
                cursor.execute("SELECT IP_INT, ACC_ID FROM CLIENT WHERE USER = '" + self.usr + "' " )
                temp_data=cursor.fetchone()
                self.client_identifier=temp_data[0]
                AID = str(temp_data[0])
                self.auth.setText("<html><head></head><body><p style=\"color:#008000;\">Authenticated</p></body></html>")
                self.ip_3.setText(AID)
                file = open("usr.dat","w")
                file.write(AID)
                file.close()
                print(self.auth_stat)

    def connect(self):
        auth_salt=self.salt.toPlainText()
        if self.auth_stat is 'Yes':

            s=socket.socket()
            port=4444
            host=self.client_identifier
            data= db.db('get_auth_salt', self.usr)
            print(data)
            if auth_salt == data:
                try:
                    fp=open("host.dat","w")
                    fp.write(self.client_identifier)
                    fp.close()
                    print("new window")
                    _thread.start_new_thread(self.new_window,())
                    sys.exit(app.exec_())

                except Exception as e:
                    print(e)
            else:
                print("check IP")


        else:
            os.system('login_ack_fal.py')

    def exit(self):
        sys.exit()

    def new_window(self):
        os.system('main_2.py')


if __name__ == '__main__':
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    prog = Mainclass(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())