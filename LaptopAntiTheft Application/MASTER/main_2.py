from PyQt5 import QtGui,QtWidgets,QtCore
from main_window_ui import Ui_MainWindow
import sys, _thread, time
import socket, os
import webbrowser


class mainclass(Ui_MainWindow):

    def __init__(self,MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        self.alarm_stat=100

        # keeping track of connection status
        self.xx = 0

        #socket for connection
        self.s = socket.socket()
        _thread.start_new_thread(self.connection,())
        self.screenshot.clicked.connect(self.screenie)
        self.alarm.clicked.connect(self.alarmthread)
        self.webcam.clicked.connect(self.webcam_stream_thread)
        self.loc.clicked.connect(self.geoloc)
        self.notify.clicked.connect(self.message)
        time.sleep(2)
        self.settext("connection")

    def geoloc(self):
        self.s.send("geolocation".encode())
        temp = self.s.recv(1024)
        temp = temp.decode()

        # it gets the confirmation from main.py of CLIENT
        if temp == "success":
            loc = open(r"D:\loc.dat",'r')
            lonlat = open(r"D:\llat.dat",'r')
            temp = lonlat.read()
            temp = temp.split()
            latitude = temp[0]
            longitude = temp[1]
            lonlat.close()
            data = loc.read()
            file = open("content.dat",'a')
            file.write('''\n==============Location Details:============== \n'''
            + data +   '''\n======================================''')
            file.close()
            self.settext("geoloc")
            try:
                # opening a new browser with google maps
                _thread.start_new_thread(webbrowser.open, ("https://www.google.com/maps/?q="+str(latitude)+","+str(longitude),))
            except Exception as e:
                print(e)
            # webbrowser.open("https://www.google.com/maps/?q="+str(latitude)+","+str(longitude))
        else:
            file = open("content.dat", 'a')
            file.write("\n[+]Retrieval Failed[+]")
            file.close()
            self.settext("geoloc")

    def settext(self,what):
        content=""
        if what == "connection":
            if self.xx==0:
                fp = open("host.dat", "r")
                wr = open("content.dat","w")
                host = fp.read()
                fp.close()
                port = 4444
                content = "Connected to " + host + " at Port : " + str(port)
                wr.write(content)
                wr.close()
                self.textEdit.setText(content)
            else:
                wr = open("content.dat", "w")
                content = "[+]Unable to Connect. Please check the connection[+]"
                self.textEdit.setText(content)
                wr.write(content)
                wr.close()

        elif what == "alarm":
            wr = open("content.dat", "a")
            wr.write("\n[+]Alarm Signal successfully Sent To Client System[+]")
            wr.close()
            wr = open("content.dat", "r")
            content = wr.read()
            wr.close()
            self.textEdit.setText(content)

        elif what == "geoloc":
            wr = open("content.dat","r")
            content = wr.read()
            wr.close()
            self.textEdit.setText(content)

    def connection(self):
        fp = open("host.dat","r")
        host = fp.read()
        fp.close()
        port = 4444
        print(host)
        try:
            self.s.connect((host,port))
        except:
            self.xx = 1000

    def alarmthread(self):
        if self.alarm_stat==1:
            self.alarm_stat=101
        self.settext("alarm")
        _thread.start_new_thread(self.alarm_, ())

    def alarm_(self):
        if self.alarm_stat==100:
            self.alarm_stat=1
            self.s.send("alarm".encode())
            self.alarm.setText("Stop Alarm")
            while 1:
                time.sleep(2)
                self.s.send("alarm".encode())
                print("ala")
                #if self.alarm_stat==101:
                    #break
        else:
            self.alarm.setText("Start Alarm")
            for i in range(1,10):
                self.s.send("stop".encode())
                time.sleep(1)
            self.alarm_stat = 100
            print("sto")

    def webcam_stream_thread(self):
        _thread.start_new_thread(self.webcam_stream,())

    def webcam_stream(self):
        print("webcam")
        self.s.send("webcam".encode())
        time.sleep(4)
        file = open("usr.dat",'r')
        ip = file.read()
        _thread.start_new_thread(webbrowser.open, ("http://"+ip+":5000",))


    def screenie(self):
        _thread.start_new_thread(self.screen,())
    def screen(self):
        print("screenshot")
        self.s.send("screenshot".encode())
        k = self.s.recv(1000)
        k=k.decode()
        print(k)
        k=int(k)
        img=self.s.recv(k)

        fp = open("image_received.jpg", "wb")
        fp.write(img)
        fp.close()
        os.system("image_received.jpg")

    def message(self):
        message_content=self.messagecontent.toPlainText()
        self.s.sendall("message".encode())
        self.s.send(message_content.encode())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    prog=mainclass(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
