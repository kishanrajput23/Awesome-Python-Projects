# Alarm clock
### Code
~~~
from tkinter import *
import datetime 
from tkinter.messagebox import *
from tkinter.ttk import * 
import winsound
MainWindow=Tk()
MainWindow.title("Alarm clock")
MainWindow.config(bg="navy blue")
MainWindow.geometry("600x300") 
def Alarm():
    if a1.get()=="AM":
        x=int(b1.get())
        y=int(b2.get())
    if a1.get()=="PM":
        x=int(b1.get())+12
        y=int(b2.get())
    showinfo("notification", "alarm has been set")
    while True:
        if x == datetime.datetime.now().hour and y == datetime.datetime.now().minute:
            print("Ringing....")
            winsound.PlaySound("punky.mp3")
            break
label1=Label(MainWindow,text="Hour:")
label2=Label(MainWindow,text="Minute:")
label1.place(relx=0.1,rely=0.1)
label2.place(relx=0.5,rely=0.1)
b1=Entry(MainWindow)
b2=Entry(MainWindow)
b1.place(relx=0.2,rely=0.1)
b2.place(relx=0.6,rely=0.1)
c1=Button(MainWindow,text="Set Alarm",command=Alarm)
c1.place(relx=0.4,rely=0.5)
a1=Combobox(MainWindow,values=["AM","PM"])
a1.place(relx=0.42,rely=0.3)
label3=Label(MainWindow,text="AM OR PM:")
label3.place(relx=0.3,rely=0.3)
mainloop()

~~~
## SS
![ss_alarmclock](https://user-images.githubusercontent.com/104223444/193425587-c5d48ca7-c554-496f-a623-b5add760f85b.png)
## Output
![Screenshot 2022-10-02 011039](https://user-images.githubusercontent.com/104223444/193425633-500fe954-ecbd-4af7-b4a8-d90e4fb3a829.png)
