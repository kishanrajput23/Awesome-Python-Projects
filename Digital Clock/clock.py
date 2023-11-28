from tkinter import * 
import time
app_window = Tk() 
app_window.title("Python Digital Clock") 
app_window.geometry("360x170") 
app_window.resizable(1,1)

text_font= ("Franklin Gothic Medium Cond", 65)
background = "#FFFFEF"
foreground= "red4"
border_width = 25

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def d_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(200, d_clock)

d_clock()
app_window.mainloop()
