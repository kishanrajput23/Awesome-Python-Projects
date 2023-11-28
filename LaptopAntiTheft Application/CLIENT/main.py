import _thread  # for multithreading
import os
import sys
import time  # for sleep method
import winsound  # Audio library
import process  # This is a custom module we wrote and saved as process.py to make this file short
import MySQLdb  # DB connectivity
from PyQt5 import QtWidgets  # For GUI of application


import cam_ip_set  # # This is a custom module we wrote and saved as process.py to make this file short

from client_gui import Ui_MainWindow  # also for GUI


class mainclass(Ui_MainWindow):

    # initializing main UI from PyQT
    def __init__(self,MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)

        # Keeping the default state to unauthenticated
        self.auth_stat="Unauthenticated"
        self.l_ip=0

        # connecting each and every function to button click
        self.FetchIP.clicked.connect(self.tip)
        self.Exit.clicked.connect(self.closeapp)

        # threading to stop unresponsive window
        _thread.start_new_thread(self.connection_status,())
        _thread.start_new_thread(self.sysinf, ())
        self.Login.clicked.connect(self.loginth)

    def tip(self):
        # starting a new thread for IP address
        _thread.start_new_thread(self.ipaddresses, ())

    def sysinf (self):
        # system information gathering
        time.sleep(2)
        processor= process.sysinfo('processor')
        type= process.sysinfo('type')
        arch= process.sysinfo('arch')
        version= process.sysinfo('ver')

        # setting the values to each labels of window
        self.processor.setText(processor)
        self.Arch.setText(arch)
        self.OS_Type.setText(type)
        self.OS.setText(version)

    def loginth(self):
        # new thread for login
        _thread.start_new_thread(self.login, ())

    def login(self):
        ''' login window
             Here if we are already authenticated, the program will not ask for authentication again '''
        if self.auth_stat is 'Authenticated':
            pass
        else:

            # Login_processor saves username and password in user.dat file
            os.system('login_processor.py')
            while True:
                if os.path.isfile('user.dat') is True:
                    print('file found')

                    # opening and reading it
                    u = open('user.dat','r+')
                    p = open('pwd.dat','r+')
                    user = u.read()
                    pwd = p.read()

                    # making the dat files blank after reading it for security purpose
                    u.truncate(0)
                    p.truncate(0)
                    u.close()
                    p.close()

                    # threading the function for authentication purpose
                    _thread.start_new_thread(self.authentication,(user,pwd))
                    break

    def authentication(self,user,pwd):
        # Database connection and login process
        db = MySQLdb.connect("localhost", "root", "toor", "credentials")
        cursor = db.cursor()

        # we declare "auth99" to see authentication status.
        self.auth99=0
        # print("SELECT * FROM LOGINS WHERE USERNAME = '" + user + "' AND PASSWORD = '" + pwd+"'")
        try:
            ''' Testing if the credentials are right or wrong
            # if auth99 = 0 --> login failed (the username & password combination are NOT there in DB)
            # if auth99 = 1 --> login success (the username & password combination are there in DB) '''

            self.auth99 = cursor.execute("SELECT * FROM CLIENT WHERE USER = '" + user + "' AND PASS = '" + pwd + "'")
        except Exception as e:
            pass
        print(self.auth99)
        if self.auth99 is 0:
            self.auth_stat="Unauthenticated"
            os.system('login_ack_fal.py')
        else:
            self.auth_stat="Authenticated"
            self.l_ip= process.get_ip_local()
            cursor.execute("SELECT * FROM CLIENT WHERE USER = '" + user + "' AND PASS = '" + pwd + "'")
            data = cursor.fetchone()
            for x in data:

                # getting key, salt username and access ID from DB
                authkey = data[3]
                authsalt = data[4]
                unam = data[0]
                aid = data[5]
            print(authsalt)

            # print("UPDATE CLIENT SET IP_INT= '" + l_ip + "' WHERE USER = '"+ user + "' AND PASS = '" + pwd + "'")
            cursor.execute("UPDATE CLIENT SET IP_INT= '" + self.l_ip + "' WHERE USER = '"+ user + "' AND PASS = '" + pwd + "'")
            cursor.connection.commit()
            self.Auth_key.setText(str(authkey))
            self.Auth_salt.setText(str(authsalt))
            self.Username.setText(unam)
            self.aid.setText(str(aid))

            # setting authenticated in green colour
            self.Auth_stat.setText("<html><head></head><body><p style=\"color:#008000;\">Authenticated</p></body></html>")

            # open LOGIN SUCCESS popup
            os.system('login_ack_scs.py')

            # another thread to start the listener using sockets
            _thread.start_new_thread(self.conn_est, ())

    def conn_est(self):

        #  runs to establish a connection using client server model
        import socket
        s=socket.socket()
        host=socket.gethostbyname(socket.gethostname())
        port=4444
        print("Skt start")
        s.bind((host,port))
        s.listen(5)
        print("listening")
        while 1:
            c, addr= s.accept()
            print("connected to "+ str(addr))
            self.after_conn_est(c)


    def after_conn_est(self,c):
        """ After the connection has been established. We use a while loop to continuously listen for the commands
         from master using RECV and DECODE function. """
        while 1:
            k=c.recv(1024)
            k=k.decode()
            # Checking if the received commands match with any of the defined IF conditions to perform predefined task
            if k == "screenshot":
                # Taking the screenshot and saving as bytes into a variable
                bytecode= process.screen_shot()
                # Saving the taken screenshot as bytes into a file
                fp=open("temp.jpg","wb")
                # Saving the size of bytestream into a variable N as well as to temp.jpg
                n=fp.write(bytecode)
                print(n)
                # converting bytestream to string for sending across network
                n=str(n)
                c.sendall(n.encode())
                fp.close()
                c.sendall(bytecode)

            elif k == "message":
                temp_message = c.recv(1024)
                temp_message = temp_message.decode()
                process.show_message(temp_message)

            elif k == "geolocation":
                loc_full_data= process.geo_location()
                print(loc_full_data)
                if loc_full_data=="timedout":
                    c.sendall("failed".encode())
                else:
                    log_split=loc_full_data.split(",")
                    city=log_split[1]
                    region=log_split[10]
                    lat=log_split[5]
                    lat1=lat.split(":")
                    lat1=lat1[1]
                    lon=log_split[6]
                    lon1=lon.split(":")
                    lon1=lon1[1]
                    file=open(r"D:\loc.dat",'w')
                    lonlat=open(r"D:\llat.dat","w")
                    file.write(city+"\n"+region+"\n"+lat+"\n"+lon)
                    lonlat.write(lat1 +"\n" + lon1)
                    lonlat.close()
                    file.close()
                    c.sendall("success".encode())

            elif k == "webcam":
                k=self.l_ip
                print(k)
                cam_ip_set.ipset(k)
                _thread.start_new_thread(self.wcstart,())

            elif k == "format":
                print("Beta Feature")

            elif k == "alarm":
                frequency=2500
                duration=1000
                while 1:
                    # for firing the beep
                    winsound.Beep(frequency,duration)
                    time.sleep(50.0/1000.0)
                    k1=c.recv(1000)
                    k1=k1.decode()
                    print(k1)
                    if k1 == "stop":
                        print("break")
                        break

            elif k == "get_file":
                pass

    def wcstart(self):
        # For webcam
        os.system("webcam.py")

    def connection_status(self):
        cs_hn= process.connection_status('hostname')
        time.sleep(3)
        self.Hostname.setText(cs_hn)
        while 1:
            cs_stat= process.connection_status('status')
            if cs_stat in 'Online':
                self.status.setText("<html><head></head><body><p style=\"color:#008000;\">Online</p></body></html>")
            else:
                self.status.setText("<html><head></head><body><p style=\"color:#ff0000;\">Offline</p></body></html>")
            time.sleep(2)

    def ipaddresses(self):
        self.E_ip.setText("Fetching")
        i_ip = process.get_ip_local()
        self.I_ip.setText(i_ip)
        try:
            e_ip = process.get_ip_public()
            self.E_ip.setText(e_ip)
        except:
            self.E_ip.setText("No Internet")

    def closeapp(self):
        sys.exit(app.exec_())


''' Here __name__ is a special attribute. Its used to pinpoint the execution point
and __name__ == __main__ says if its a main function then execute it'''
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    prog=mainclass(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



# IGNORE IT


# if a<4:
# 	s.send("screenshot".encode())
# 	k=s.recv(1000)
# 	k=k.decode()
# 	k=int(k)
# 	by=s.recv(k)
#
# > fp=open(r"E:/ffff.jpg","wb")
# >>> fp.write(by)
# 94725
# >>> f.close()
# >>> fp.close()
# >>>