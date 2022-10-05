import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry("1360x360+0+0")
root.resizable(0,0)
root.config(background="silver")
root.title("INVENTORY MANAGEMENT SYSTEM")

# Inventory_management_frame
Inventory_management_frame = LabelFrame(root, text="Inventory Management",background="silver",height= 315, width=280,font=("arial",13,"bold"))
Inventory_management_frame.place(x=10,y=20,width=280, height=335)

# labels
ip_id = tk.Label(Inventory_management_frame,text= "Product id:",justify=RIGHT, background= "silver",fg= "black",font=("times new roman", 14,"bold"))
ip_id.place(x=20,y=10)

# text
entry1 = ttk.Entry(Inventory_management_frame, width=15,font=("times new roman", 14))
entry1.place(x=20,y=40,width=200)

# labels
ip_name = tk.Label(Inventory_management_frame,text= "Product name:",background= "silver",fg= "black",font=("times new roman", 14,"bold") )
ip_name.place(x=20,y=70)

# text
entry2 = ttk.Entry(Inventory_management_frame, width=15,font=("times new roman", 14))
entry2.place(x=20,y=100,width=200)

# labels
ip_price = tk.Label(Inventory_management_frame,text= "Selling price:",background= "silver",fg= "black",font=("times new roman", 14,"bold") )
ip_price.place(x=20,y=130)

# text
entry3 = ttk.Entry(Inventory_management_frame, width=15,font=("times new roman", 14))
entry3.place(x=20,y=160,width=200)

# labels
ip_quantity = tk.Label(Inventory_management_frame,text= "Quantity:",background= "silver",fg= "black",font=("times new roman", 14,"bold") )
ip_quantity.place(x=20,y=190)

# text
entry4 = ttk.Entry(Inventory_management_frame, width=15,font=("times new roman", 14))
entry4.place(x=20,y=220,width=200)

# table frame
Table_frame= LabelFrame(root, text="Product List", background="silver",height=315, width=1066,font=("arial",13,"bold"))
Table_frame.place(x=295,y=20,width=1061, height=335)

Table=ttk.Treeview(root,columns=("inp_id","inp_name","inp_price","inp_quantity"))
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview",background="white",fieldbackground="white",)
Table.heading('#0',text="Item no", anchor ='w')
Table.heading("inp_id",text="Product id", anchor ='w')
Table.heading("inp_name",text="Name", anchor ='w')
Table.heading("inp_price",text="Selling price", anchor ='w')
Table.heading("inp_quantity",text="Quantity", anchor ='w')
Table.column('#0',width=190)
Table.column("inp_id",width=170)
Table.column("inp_name",width=230)
Table.column("inp_price",width=200)
Table.column("inp_quantity",width=180)
Table.place(x=296,y=40,width=1055, height=313)

# function
def insert():
    ip_id = str(entry1.get())
    ip_name = str(entry2.get())
    ip_price = str(entry3.get())
    ip_quantity = str(entry4.get())
    if len(ip_id)!=0 and len(ip_id)<=100 :
        check=open("inventory_management.txt","a")
        check1 = open("inventory_management.txt", "r")
        test = check1.read()

        if ip_id in test:
            messagebox.showwarning("Already Exist","Product id already exist.Don't try to duplicate.")
        
        else:
            final_data=ip_id+","+ip_name+","+ip_price+","+ip_quantity+"\n"
            check.write(final_data)
            check.close()
            messagebox.showinfo("Information","Product details saved succesfully")

    elif (not(ip_id and ip_name and ip_price and ip_quantity.strip())) :
        messagebox.showwarning("Warning","Fields are empty")
        
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    entry4.delete(0, tk.END)

def show():
    check = open('inventory_management.txt',"r")
    Table.delete(*Table.get_children())
    line = check.readline().split(",")
    lineNum=1
    while line!="":
        Table.insert('','end',text=str(lineNum), values=(line[0],line[1],line[2],line[3]))
        line = check.readline().split(",")
        lineNum+=1
    check.close()

# button
insert = Button(Inventory_management_frame, text="Insert",command=insert,width=12,background= "crimson",fg= "white",font=("arial",10,"bold")).place(x=20,y=262)
show = Button(Inventory_management_frame, text="Show",command=show, width=12,background= "crimson",fg= "white",font=("arial",10,"bold")).place(x=130,y=262)

root.mainloop()
