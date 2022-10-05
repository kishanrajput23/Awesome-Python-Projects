import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("440x580+0+0")
root.resizable(0,0)
root.config(background="dimgrey")
root.title("MOBILE NUMBER MODULE")

# message_1
info = tk.Label(root,text="ENTER YOUR DETAILS HERE",background= "dimgrey",fg= "black",font=("arial",15,"bold"))
info.grid(row=0, columnspan=2, padx=10, pady=10)

# labels
ip_name = tk.Label(root,text= "Enter Name",background= "dimgrey",fg= "black",font=("times new roman",15,"bold") )
ip_name.grid(row=1, column=0, padx=10, pady=10)


# name text
entry1 = ttk.Entry(root, width=20,font=("times new roman", 14))
entry1.grid(row=1, column=1)

# labels
ip_number = tk.Label(root,text= "Enter Number",background= "dimgrey",fg= "black",font=("times new roman", 15,"bold") )
ip_number.grid(row=2, column=0, padx=10, pady=10)

# number text
entry2 = ttk.Entry(root, width=20,font=("times new roman", 14))
entry2.grid(row=2, column=1)

# table frame
Table_frame=Frame(root,bd=4,relief=RIDGE,bg="dimgrey")
Table_frame.grid(row= 6,pady=10,padx=10,columnspan=2)

# text
inp_text1 = tk.Text(Table_frame, height=11, width=45,background= "silver",font=("times new roman", 14))
inp_text1.grid(row=6, columnspan=2)

# message_2
statement = tk.Label(root,text="VIEW YOUR DETAILS HERE",background= "dimgrey",fg= "black",font=("arial",15,"bold"))
statement.grid(row=4, columnspan=2, padx=10, pady=10)

# function
def insert():
    inp_name = str(entry1.get())
    inp_number = str(entry2.get())

    if len(inp_number) == 10:
        check = open("users_numbers.txt", "a")
        check1 = open("users_numbers.txt", "r")
        test = check1.read()

        if inp_number in test:
            messagebox.showinfo("Already Exist","number already exist")
        
        
        else:
            check.write(f"{inp_name}\t\t{inp_number}\n")
            messagebox.showinfo("Information","number saved")
            
    elif (not(inp_name and inp_number.strip())) :
        messagebox.showwarning("Warning","Fields are empty")

    elif inp_number ==str(inp_number):
        messagebox.showwarning("Warning","Please give correct enteries")
    
    


    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

def check():
    check = open("users_numbers.txt", "r")
    rest = check.read()
    inp_text1.delete(0.0, tk.END)

    for a in rest[::-1]:
        inp_text1.insert(0.0,a)
        
def clear():
     inp_text1.delete(0.0, tk.END)
    
insert = Button(root, text="Insert", command=insert ,width=12,background= "crimson",fg= "white",font=("arial",10,"bold")).grid(row= 3,pady=10,columnspan=2)
check = Button(root, text="Check", command=check, width=12,background= "navy",fg= "white",font=("arial",10,"bold")).grid(row= 5, column=0,pady=10)
clear1 = Button(root, text="Clear", command= clear, width=12,background= "navy",fg= "white",font=("arial",10,"bold")).grid(row= 5, column=1,pady=10)
root.mainloop()
