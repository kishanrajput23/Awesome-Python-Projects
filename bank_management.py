import mysql.connector as m
import sys
import time
import csv
from datetime import date

# THIS WILL CREATE TABLE AND START THE PROGRAM

def table_create():
    print("Is it your first time running this program ?")
    print()
    print("If yes, press 1")
    print("If not, press 2")
    print()      
    print()
    try:
        tm = int(input("Enter your choice :~ "))
    except:
        print()
        print("⚠ Wrong Input ⚠")
        print()
        print()
        print("If you wish to go back, press m, else press any key")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            table_create()
        else:
            exitdes()
            
        
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()

    global psswd
    global mydb
    global mycursor
    
    
    if tm == 1:
        try:
            mycursor.execute("create database bank_mang;")
            mycursor.execute("use bank_mang")
            mycursor.execute("create table Per_Detail(Acc_no varchar(20) primary key, Cust_name varchar(20), Cust_phone varchar(10),Cust_alt_phone varchar(10), Adhar_no varchar(12), Address_res varchar(100),Address_ofc varchar(100));")
            mycursor.execute("create table Acc_Detail(Acc_no varchar(20) primary key, Cust_name varchar(20), Acc_type varchar(8), Acc_Balance varchar(5000), Acc_Limit varchar(5000), Acc_transac varchar(5000));")
            #mycursor.execute("insert into acc_detail values('110000231','test',NULL,NULL,NULL,NULL);")
            #mycursor.execute("insert into per_detail values('110000231','test',NULL,NULL,NULL,NULL,NULL);")
        except:
            print()
            print("⚠ Wrong Input ⚠")
            print()
            print()
            print("If you wish to go back, press m, else press any key")
            print()
            mn = input("Enter your choice :~ ")
            print()
            print()
            if mn == "m" or mn == "M":
                table_create()
            else:
                exitdes()

            
        mydb.commit()
        welcome()
        acc_num()
        fh = open("trans.csv","w")
        main_menu()
       # goback()
        print()
        print()
        print()
        print()
    elif tm == 2:
        try:
            mycursor.execute("use bank_mang;")
        except:
            print()
            print("⚠ Wrong Input ⚠")
            print()
            print()
            print("If you wish to go back, press m, else press any key")
            print()
            mn = input("Enter your choice :~ ")
            print()
            print()
            if mn == "m" or mn == "M":
                table_create()
            else:
                exitdes()
            
        welcome()
        main_menu()
        #goback()
    else:
        print()
        print("⚠ Wrong Input ⚠")
        print()
        print()
        print("If you wish to go back, press m, else press any key")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            table_create()
        else:
            exitdes()

            
        

        print()
        print()
        print()
        print()

            
    
    """except m.errors.ProgrammingError :
        print()
        print()
        print("⚠ Wrong Password ⚠")
        print()
        table_create()
    except m.errors.DatabaseError:
        print()
        print()
        print("⚠ Wrong Input ⚠")
        print()
        table_create()"""
    

            
            
    
        
        



def welcome():
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("                                        ✠◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼✠")
    print("                                        ◼                                                                ◼")
    print("                                        ◼                Welcome to Bank Management Program              ◼")
    print("                                        ◼                                                                ◼")
    print("                                        ◼            BY :~ (Lalit, Harmohit, Devansh) of class 12        ◼")
    print("                                        ◼                                                                ◼")
    print("                                        ◼                                                                ◼")
    print("                                        ◼                                                         © 2020 ◼")
    print("                                        ✠◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼ ◼✠")
    print() 
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()


# MAIN MENU

def main_menu():
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("                                                                      ⚜ MAIN MENU ⚜")
    print()
    print("☢ Press 1 for Personal Details Menu ☢")
    print()
    print("☢ Press 2 for Account Details Menu  ☢")
    print()
    print()
    print("〽 To exit press enter 〽")
    print()
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    try:
        ch = int(input("Enter your choice :~ "))
        print()
        print()
        print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
        print()
        print()
        
    except:
        goback()
    if ch == 1:
        pers_detail()
    elif ch == 2:
        acc_detail()
    else:
        goback()
        """time.sleep(2)
        print()
        print()
        print("                       ✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠  【E】 【N】 【D】  ✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠")
        print()
        print()
        print("✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧")
        sys.exit()"""

        """
        print()
        print("⚠ Wrong Input ⚠")
        print()
        print("If you wish to go back to main menu, press m, else press any key")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            main_menu()

        """
    
"""
    else:
        print()
        print("⚠ Wrong Input ⚠")
        print()
        print("If you wish to go back to main menu, press m, else press any key")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            main_menu()
            """

def pers_detail():
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("     ⚜ PERSONAL DETAIL MENU ⚜")
    print()
    print()
    print("☢ Press 1 to view personal details ☢")
    print()
    print("☢ Press 2 to update details        ☢")
    print()
    try:
        ip = int(input("Enter your choice :~ "))
        
    except:
        goback()
    if ip == 1:
        view_pers_detail()
    elif ip == 2:
        upd_detail()
    else:
        goback()
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    
    """else:
        print()
        print("⚠ Wrong Input ⚠")
        print()
        print("If you wish to go back to main menu, press m, else press any key")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            main_menu()"""

        
    
    
def acc_detail():
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("     ⚜ ACCOUNT DETAIL MENU ⚜")
    print()
    print()
    print("☢ Press 1 to view Account Balance     ☢")
    print()
    print("☢ Press 2 to search an account        ☢")
    print()
    print("☢ Press 3 to delete an account        ☢")
    print()
    print("☢ Press 4 to DEPOSIT                  ☢")
    print()
    print("☢ Press 5 to WITHDRAW                 ☢")
    print()
    print("☢ Press 6 to view transactions detail ☢")
    print()
    print("☢ Press 7 to create new account       ☢")
    
    print()
    print()
    try:
        ip = int(input("Enter your choice :~ "))
        
    except:
        goback()
        """
        print()
        print("⚠ Wrong Input ⚠")
        print()
        print("If you wish to go back to account detail menu, press m, else press any key")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            acc_detail()"""
    if ip == 1:
        view_acc_bal()
    elif ip == 2:
        search_acc()
    elif ip == 3:
        delete_acc()
    elif ip == 4:
        deposit()
    elif ip == 5:
        withdraw()
    elif ip == 6:
        acc_trans()
    elif ip == 7:
        create_new_acc()
    
    else:
        goback()
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    
        
    """else:
        print()
        print("⚠ Wrong Input ⚠")
        print()
        print("If you wish to go back to main menu, press m, else press any key")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            main_menu()"""



# PERSONAL DETAIL MENU, SUB-MENUS

def view_pers_detail():
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("      〽 VIEW PERSONAL DETAIL MENU 〽")
    print()
    print("☢ Press 1 to view all customers details    ☢")
    print()
    print("☢ Press 2 to view specific person's detail ☢")
    print()
    try:
        inp = int(input("Enter your choice :~ "))
    except:
        print()
        print("⚠ Wrong Input ⚠")
        print()
        print()
        goback()
        
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    if inp == 1:
        view_all_cus_detail()
    elif inp == 2:
        view_spec_cus_detail()
    else:
        goback()
    """else:
        print()
        print("⚠ Wrong Input ⚠")
        print()
        print("If you wish to go back to main menu, press m, else press any key")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            main_menu()"""
    







def upd_detail():
    global psswd
    global mydb
    global mycursor
    #global tm
    global z
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("      〽 UPDATE PERSONAL DETAIL MENU 〽")
    print()
    try:
        z = int(input("Enter account number of the customer you want to update detail of :~ "))
    except:
        print()
        print()
        print("⚠ Invailid Account Number ⚠")
        print()
        print("If you wish to return to update personal detail menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            upd_detail()
        else:
            goback()
    print()
    print()
    hs()
    
    
    try:
        
        mycursor.execute("use bank_mang;")
    
        mycursor.execute("select * from per_detail where Acc_no = '"+str(z)+"' ;")
        tb = mycursor.fetchall()
        mydb.commit()
        print()
        
        x = ()
        for i in tb:
            x = i[0] 
        if x == ():
            print()
            print()
            print("⚠ Account Number Not Found ⚠")
            print()
            print("If you wish to return to update personal detail menu - press m, If not press any key :~ ")
            print()
            v = input("Enter your choice :~ ")
            print()
            if v == "m" or v == "M":
                upd_detail()
                print()
            else:
                main_menu()
            
        print()
        print()
        print("⫸ Press respective key to update respective detail ⫷")
        print()
        print("1. Customer name")
        print("2. Customer phone number")
        print("3. Customer alternate phone number")
        print("4. Customer residential address")
        print("5. Customer office address")
        print()
        try:
            ch = int(input("Enter your choice :~ "))
        except:
            print()
            print()
            print("⚠ Wrong choice ⚠")
            print()
            print("If you wish to return to update personal detail menu - press m, If not press any key :~ ")
            print()
            mn = input("Enter your choice :~ ")
            print()
            print()
            if mn == "m" or mn == "M":
                upd_detail()
            else:
                goback()
            
        print()
        print()
        if ch == 1:
            print()
            z1 = input("Enter new name :~ ")
            mycursor.execute("use bank_mang;")
            mycursor.execute("update per_detail set cust_name = "+"'"+str(z1)+"'"+" where acc_no = "+str(z)+";")
            mydb.commit()
            print()
            print("✔ Success ✔")
            print()
            hs()
        elif ch == 2:
            print()
            try:
                z2 = int(input("Enter new phone number :~ "))
            except:
                print()
                print()
                print("⚠ Invailid Phone Number ⚠")
                print()
                print("If you wish to return to update personal detail menu - press m, If not press any key :~ ")
                print()
                mn = input("Enter your choice :~ ")
                print()
                print()
                if mn == "m" or mn == "M":
                    upd_detail()
                else:
                    goback()
                    
            if len(str(z2)) != 10:
                print()
                print("⚠ Invalid Phone Number ⚠")
                print()
                v = input("Press m to continue, if not press enter :~ ")
                if v == "m" or v == "M":
                    upd_detail()
                    print()
                else:
                    goback()

            mycursor.execute("use bank_mang;")
            mycursor.execute("update per_detail set cust_phone = "+"'"+str(z2)+"'"+" where acc_no = "+str(z)+";")
            mydb.commit()
            print()
            print("✔ Success ✔")
            print()
            hs()
        elif ch == 3:
            print()
            try:
                z3 = int(input("Enter new alternate phone number :~ "))
            except:
                print()
                print()
                print("⚠ Invailid Alternate Phone Number ⚠")
                print()
                print("If you wish to return to update personal detail menu - press m, If not press any key :~ ")
                print()
                mn = input("Enter your choice :~ ")
                print()
                print()
                if mn == "m" or mn == "M":
                    upd_detail()
                else:
                    goback()
            if len(str(z3)) != 10:
                print()
                print("⚠ Invalid Alternate Phone Number ⚠")
                print()
                v = input("Press m to continue, if not press enter :~ ")
                if v == "m" or v == "M":
                    upd_detail()
                    print()
                else:
                    goback()

            mycursor.execute("use bank_mang;")
            mycursor.execute("update per_detail set cust_alt_phone = "+"'"+str(z3)+"'"+" where acc_no = "+str(z)+";")
            mydb.commit()
            print()
            print("✔ Success ✔")
            print()
            hs()
        elif ch == 4:
            print()
            z4 = int(input("Enter new residential address :~ "))
            mycursor.execute("use bank_mang;")
            mycursor.execute("update per_detail set address_res = "+"'"+str(z4)+"'"+" where acc_no = "+str(z)+";")
            mydb.commit()
            print()
            print("✔ Success ✔")
            print()
            hs()
        elif ch == 5:
            print()
            z5 = int(input("Enter new office address :~ "))
            mycursor.execute("use bank_mang;")
            mycursor.execute("update per_detail set address_ofc = "+"'"+str(z5)+"'"+" where acc_no = "+str(z)+";")
            mydb.commit()
            print()
            print("✔ Success ✔")
            print()
            hs()
        else:
            print()
            print()
            print("⚠ Wrong Choice ⚠")
            print()
            print("If you wish to return to update personal detail menu - press m, If not press any key :~ ")
            print()
            mn = input("Enter your choice :~ ")
            print()
            print()
            if mn == "m" or mn == "M":
                upd_detail()
            else:
                goback()
        print()
        print()
        print("If you wish to update more records - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            upd_detail()
        else:
            goback()
    
            
    except :
        print("⚠ Wrong Account Number ⚠")
        print()
        print("If you wish to return to update personal detail menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            upd_detail()
        else:
            goback()
    
        """else:
            print()
            print("⚠ Wrong Input ⚠")
            print()
            print("If you wish to go back to main menu - press m \nIf you return to personal detail update menu - press u \nIf you want to exit - press any key")
            print()
            mn = input("Enter your choice :~ ")
            print()
            print()
            if mn == "m" or mn == "M":
                main_menu()
            elif mn == "u" or mn == "U":
                upd_detail()"""
    
    
        
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
        
def hs():
    global psswd
    global mydb
    global mycursor
    global tm
    mycursor.execute("use bank_mang;")
    mycursor.execute("select * from per_detail where acc_no = "+str(z)+";")
    tb = mycursor.fetchall()
    mydb.commit()
    for i in tb:
        print(i)
        



# PERSONAL DETAIL MENU K SUB MENU KA SUB MENU 1st WALA

def view_all_cus_detail():
    global psswd
    global mydb
    global mycursor
    global tm
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("      〽 VIEW ALL COUSTOMERS PERSONAL DETAIL 〽")
    print()
    mycursor.execute("use bank_mang;")
    mycursor.execute("select * from per_detail;")
    tb = mycursor.fetchall()
    mydb.commit()
    print()
    for i in tb:
        print(i)
    print()
    print("✔ Success ✔")
    print()
    print()
    #table_create
    """print("If you wish to go back to main menu, press m, else press any key")
    print()
    mn = input("Enter your choice :~ ")
    print()
    print()
    
    if mn == "m" or mn == "M":
        main_menu()"""
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    time.sleep(5)
    goback()
    

def view_spec_cus_detail():
    global psswd
    global mydb
    global mycursor
    global tm
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("      〽 VIEW SPECIFIC COUSTOMERS PERSONAL DETAIL 〽")
    print()
    try:
        ac = int(input("Enter the account no. of the customer you want to view personal detail of :~ "))
        print()
    except:
        print()
        print("⚠ Invalid Account Number ⚠")
        print()
        print("If you wish to return to view specific personal detail menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            view_spec_cus_detail()
        else:
            goback()


    mycursor.execute("use bank_mang;")
    
    mycursor.execute("select * from per_detail where Acc_no = '"+str(ac)+"' ;")
    tb = mycursor.fetchall()
    mydb.commit()
    print()
    x = ()
    for i in tb:
        print(i)
        x = i[0] 
    if x == ():
        print()
        print()
        print("⚠ Account Number Not Found ⚠")
        print()
        print("If you wish to return to view specific personal detail menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            view_spec_cus_detail()
        else:
            goback()
        
    print()
    print("✔ Success ✔")
    print()
    print()

    v = input("Press m to view more record, if not press enter :~ ")
    if v == "m" or v == "M":
        view_spec_cus_detail()
        print()
    else:
        goback()
    
        
        
    
    
    #main_menu()
    """print("If you wish to go back to main menu, press m, else press any key")
    print()
    mn = input("Enter your choice :~ ")
    print()
    print()
    if mn == "m" or mn == "M":
        main_menu()"""
"""
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    time.sleep(5)
    main_menu()"""


# ACCOUNT DETAIL MENU, SUB-MENU




def view_acc_bal():
    global psswd
    global mydb
    global mycursor
    global tm
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("      〽 VIEW ACCOUNT BALANCE 〽")
    print()
    try:
        ac = int(input("Enter the account no. of the customer you want to view account balance of :~ "))
        print()
    except:
        print()
        print("⚠ Invalid Account Number ⚠")
        print()
        print("If you wish to return to view account balance - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            view_acc_bal()
        else:
            goback()


    mycursor.execute("use bank_mang;")
    
    mycursor.execute("select acc_balance from acc_detail where Acc_no = '"+str(ac)+"' ;")
    tb = mycursor.fetchall()
    mydb.commit()
    print()
    x = ()
    for i in tb:
        print(i)
        x = i[0] 
    if x == ():
        print()
        print()
        print("⚠ Account Number Not Found ⚠")
        print()
        print("If you wish to return to view account balance - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            view_acc_bal()
        else:
            goback()
        
    print()
    print("✔ Success ✔")
    print()
    print()

    v = input("Press m to view more record, if not press enter :~ ")
    if v == "m" or v == "M":
        view_acc_bal()
        print()
    else:
        goback()





def search_acc():
    global psswd
    global mydb
    global mycursor
    global tm
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("      〽 SEARCH ACCOUNT 〽")
    print()
    try:
        ac = int(input("Enter the account no. of the customer you want to view account detail of :~ "))
        print()
    except:
        print()
        print("⚠ Invalid Account Number ⚠")
        print()
        print("If you wish to return to search account menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            search_acc()
        else:
            goback()


    mycursor.execute("use bank_mang;")
    
    mycursor.execute("select * from acc_detail where Acc_no = '"+str(ac)+"' ;")
    tb = mycursor.fetchall()
    mydb.commit()
    print()
    x = ()
    for i in tb:
        print(i)
        x = i[0] 
    if x == ():
        print()
        print()
        print("⚠ Account Number Not Found ⚠")
        print()
        print("If you wish to return to search account menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            search_acc()
        else:
            goback()
        
    print()
    print("✔ Success ✔")
    print()
    print()

    v = input("Press m to view more record, if not press enter :~ ")
    if v == "m" or v == "M":
        search_acc()
        print()
    else:
        goback()
    
    
def delete_acc():
    #global psswd
    global mydb
    global mycursor
    #global tm
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("      〽 DELETE ACCOUNT 〽")
    print()
    try:
        ac = int(input("Enter the account no. of the customer you want to delete account of :~ "))
        print()
    except:
        print()
        print("⚠ Invalid Account Number ⚠")
        print()
        print("If you wish to return to delete account menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            delete_acc()
        else:
            goback()


    mycursor.execute("use bank_mang;")
    
    
    print()
    mycursor.execute("select * from per_detail where Acc_no = '"+str(ac)+"' ;")
    tb = mycursor.fetchall()
    mydb.commit()
    print()
    x = ()
    for i in tb:
        print(i)
        x = i[0] 
    if x == ():
        print()
        print()
        print("⚠ Account Number Not Found ⚠")
        print()
        print("If you wish to return to delete account menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            delete_acc()
        else:
            goback()
        


    mycursor.execute("delete from acc_detail where Acc_no = '"+str(ac)+"' ;")
    mycursor.execute("delete from per_detail where Acc_no = '"+str(ac)+"' ;")
    mydb.commit()
    print()
    print()
    print("✔ Delete Success ✔")
    print()
    print()

    v = input("Press m to delete more record, if not press enter :~ ")
    if v == "m" or v == "M":
        delete_acc()
        print()
    else:
        goback()


        
    
    
def deposit():
    global mycursor
    global mydb
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("〽 Deposit Menu 〽")
    print()
    print()
    try:
        ac = int(input("Enter the account no. of the customer you want to Deposit in :~ "))
        print()
    except:
        print()
        print("⚠ Invalid Account Number ⚠")
        print()
        print("If you wish to return to Deposit menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            deposit()
        else:
            goback()
    mycursor.execute("use bank_mang;")
    mycursor.execute("select acc_balance from acc_detail where acc_no ="+str(ac)+";")
    tb = mycursor.fetchall()
    mydb.commit
    if tb == []:
        print()
        print()
        print("⚠ Account Number Not Found ⚠")
        print()
        print("If you wish to return to Deposit menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            deposit()
        else:
            goback()
    print()
    print()
    try:
        amt = int(input("Enter the amount you want to Deposit :~ "))
        print()
    except:
        print()
        print("⚠ Invalid Deposit Amount ⚠")
        print()
        print("If you wish to return to Deposit menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            deposit()
        else:
            goback()
    mycursor.execute("select acc_limit from acc_detail where acc_no ="+str(ac)+";")
    tc = mycursor.fetchall()
    if int(tc[0][0]) < amt:
        print()
        print()
        print("⚠ Transaction Error : Limit Exceeded ⚠")
        print()
        print("If you wish to return to Deposit menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            deposit()
        else:
            goback()
    mycursor.execute("update acc_detail set acc_balance = acc_balance + "+str(amt)+" where acc_no = "+str(ac)+";")
    mycursor.execute("update acc_detail set acc_transac = acc_transac + 1 where acc_no = "+str(ac)+";")

    mydb.commit()
    print()
    print()
    print("   ✔ Transaction Successful ✔")
    print()
    print()
    fh = open("trans.csv","a")
    f = csv.writer(fh)
    d = date.today()
    c = "Credited"
    l = []
    l.append(ac)
    l.append(amt)
    l.append(c)
    l.append(d)
    f.writerow(l)
    fh.close()
    vz = input("Press m to deposit more ammount, if not press enter :~ ")
    print()
    if vz == "m" or vz == "M":
        deposit()
        print()
    else:
        print()
        print()
        print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
        print()
        print()
        goback()
    
    
    
    
        
    

def withdraw():
    global mycursor
    global mydb
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("〽 Withdraw Menu 〽")
    print()
    print()
    try:
        ac = int(input("Enter the account no. of the customer you want to Withdraw from :~ "))
        print()
    except:
        print()
        print("⚠ Invalid Account Number ⚠")
        print()
        print("If you wish to return to Withdraw menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            withdraw()
        else:
            goback()
    mycursor.execute("use bank_mang;")
    mycursor.execute("select acc_balance from acc_detail where acc_no ="+str(ac)+";")
    tb = mycursor.fetchall()
    mydb.commit
    if tb == []:
        print()
        print()
        print("⚠ Account Number Not Found ⚠")
        print()
        print("If you wish to return to Withdraw menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            withdraw()
        else:
            goback()
    print()
    print()
    try:
        amt = int(input("Enter the amount you want to Withdraw :~ "))
        print()
    except:
        print()
        print("⚠ Invalid Withdraw Amount ⚠")
        print()
        print("If you wish to return to Withdraw menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            withdraw()
        else:
            goback()
    if int(tb[0][0]) < amt:
        print()
        print()
        print("⚠ Transaction Error : Insufficent Funds ⚠")
        print()
        print("If you wish to return to Withdraw menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            withdraw()
        else:
            goback()
    mycursor.execute("update acc_detail set acc_balance = acc_balance - "+str(amt)+" where acc_no = "+str(ac)+";")
    mycursor.execute("update acc_detail set acc_transac = acc_transac + 1 where acc_no = "+str(ac)+";")
    mydb.commit()
    print()
    print()
    print("   ✔ Transaction Successful ✔")
    print()
    print()
    fh = open("trans.csv","a")
    f = csv.writer(fh)
    d = date.today()
    c = "Debited"
    l = []
    l.append(ac)
    l.append(amt)
    l.append(c)
    l.append(d)
    f.writerow(l)
    fh.close()
    vz = input("Press m to withdraw more ammount, if not press enter :~ ")
    print()
    if vz == "m" or vz == "M":
        withdraw()
        print()
    else:
        print()
        print()
        print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
        print()
        print()
        goback()


def acc_trans():
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("〽 Transaction Detail Menu 〽")
    print()
    print()
    try:
        ac = int(input("Enter the account no. of the customer you want to view transaction detail of :~ "))
        print()
    except:
        print()
        print("⚠ Invalid Account Number ⚠")
        print()
        print("If you wish to return to transaction detail menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            acc_trans()
        else:
            goback()
    mycursor.execute("use bank_mang;")
    mycursor.execute("select acc_balance from acc_detail where acc_no ="+str(ac)+";")
    tb = mycursor.fetchall()
    mydb.commit
    if tb == []:
        print()
        print()
        print("⚠ Account Number Not Found ⚠")
        print()
        print("If you wish to return to transaction detail menu - press m, If not press any key :~ ")
        print()
        mn = input("Enter your choice :~ ")
        print()
        print()
        if mn == "m" or mn == "M":
            acc_trans()
        else:
            goback()
    print()
    print()
    fh = open("trans.csv","r")
    f = csv.reader(fh)
    for i in f:
        if i == []:
            pass
        elif i[0] == str(ac):
            print(i)
        
            
        
    print()
    print() 
    fh.close()
    vz = input("Press m to view more transaction, if not press enter :~ ")
    print()
    if vz == "m" or vz == "M":
        acc_trans()
        print()
    else:
        print()
        print()
        print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
        print()
        print()
        goback()
    

def create_new_acc():
    global psswd
    global mydb
    global mycursor
    #global tm
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    print("〽 Create New Account Menu 〽")
    print()
    print()
    print()
    print("   ⚜ Fill Personal Details ⚜")
    print()
    print("‼  All Information is compulsory to fill  ‼")
    print()
    print()
    ac = acc_num_2()
    print("Account Number Alotted :~ ",ac)
    print()

    cname = input("Enter Customer Name :~ ")
    if len(cname) == 0:
        
        print()
        print()
        print("⚠ Invalid Customer Name ⚠")
        print()
        
        v = input("Press m to continue, if not press enter :~ ")
        if v == "m" or v == "M":
            create_new_acc()
            print()
        else:
            goback()
        print()
    try:   
        cph = int(input("Enter Customer Phone Number(10) :~ "))
    except:
        print()
        print("⚠ Invalid Phone Number ⚠")
        print()
        v = input("Press m to continue, if not press enter :~ ")
        if v == "m" or v == "M":
            create_new_acc()
            print()
        else:
            goback()
        
        
        
    if len(str(cph)) != 10:
        print()
        print("⚠ Invalid Phone Number ⚠")
        print()
        v = input("Press m to continue, if not press enter :~ ")
        if v == "m" or v == "M":
            create_new_acc()
            print()
        else:
            goback()

    try:
        cap = int(input("Enter Customer Alternate Phone Number :~ "))
    except:
        print()
        print("⚠ Invalid Alternate Phone Number ⚠")
        print()
        v = input("Press m to continue, if not press enter :~ ")
        if v == "m" or v == "M":
            create_new_acc()
            print()
        else:
            goback()
            
    if len(str(cap)) != 10:
        print()
        print("⚠ Invalid Alternate Phone Number ⚠")
        print()
        v = input("Press m to continue, if not press enter :~ ")
        if v == "m" or v == "M":
            create_new_acc()
            print()
        else:
            goback()

    
    try:
        cad = int(input("Enter Customer Adhar Number(12) :~ "))
    except:
        print()
        print("⚠ Invalid Adhar Number ⚠")
        print()
        v = input("Press m to continue, if not press enter :~ ")
        if v == "m" or v == "M":
            create_new_acc()
            print()
        else:
            goback()
    if len(str(cad)) != 12:
        print()
        print("⚠ Invalid Adhar Number ⚠")
        print()
        v = input("Press m to continue, if not press enter :~ ")
        if v == "m" or v == "M":
            create_new_acc()
            print()
        else:
            goback()
    car = input("Enter Coustomer Residential Address :~ ")
    cao = input("Enter Coustomer Office Address :~ ")
    print()
    print()
    print("   ⚜ Fill Account Details ⚜")
    print()
    print("‼  All Information is compulsory to fill  ‼")
    print()
    print()
    cat = input("Enter Account Type (S for Saving Account || C for Current Account) :~ ")
    if cat == "s" or cat == "S":
        cat = "SAVING"
    elif cat == "c" or cat == "C":
        cat = "CURRENT"
    else :
        print()
        print("⚠ Invalid Account type ⚠")
        print()
        v = input("Press m to continue, if not press enter :~ ")
        if v == "m" or v == "M":
            create_new_acc()
            print()
        else:
            goback()
    cab = 0
    try:
        acl = int(input("Enter Account limit (In Digits) :~ "))
    except:
        print()
        print("⚠ Invalid Account Limit ⚠")
        print()
        v = input("Press m to continue, if not press enter :~ ")
        if v == "m" or v == "M":
            create_new_acc()
            print()
        else:
            goback()
        
    act = 0
    mycursor.execute("use bank_mang;")
    mycursor.execute('insert into per_detail values('+'\"'+str(ca)+'\"'+','+'\"'+cname+'\"'+','+'\"'+str(cph)+'\"'+','+'\"'+str(cap)+'\"'+','+'\"'+str(cad)+'\",\"'+car+'",'+'"'+cao+'\"'+')')
    mycursor.execute('insert into acc_detail values('+'\"'+str(ca)+'\"'+','+'\"'+cname+'\"'+',\"'+cat+'\",'+str(cab)+','+str(acl)+','+'\"'+str(act)+'\")')
    mydb.commit()
    fh1 = open("accno.txt","w+")
    fh1.write(str(ca))
    fh1.close()
    
    print()
    print("✔ RECORD SUCCESSFULLY ADDED ✔")
    print()
    print()
    vz = input("Press m to add more record, if not press enter :~ ")
    print()
    if vz == "m" or vz == "M":
        create_new_acc()
        print()
    else:
        print()
        print()
        print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
        print()
        print()
        goback()
    









    
# account number generator


def acc_num():
    ca = 110000231
    fh = open("accno.txt","w+")
    fh.write(str(ca))
    fh.close()
    

def acc_num_2():
    global ca
    zh = open("accno.txt","r")
    ca = int(zh.read())
    ca += 1
    zh.close()
    return ca

#################################
    
    



# WHEN USER TRY TO EXIT, THIS WILL OPEN

def goback():
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    xx = input("If you wish to go back to main menu, press m\nIf you wish to exit, press enter\nEnter your choice :~ ")
    if xx == "m" or xx == "M":
        print()
        print()
        print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
        print()
        print()
        main_menu()
    else:
        exitdes()
    

###############################


    

# FIRST FUCNTION TO BE RUN

def entry():
    global mydb
    global mycursor
    print()
    print()
    print("➰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰〰➰")
    print()
    print()
    psswd = input("Enter your Mysql password :~ ")
    print()
    print()
    
    try:
        mydb = m.connect(host = "localhost", user = "root", password = psswd)
        mycursor = mydb.cursor()
    except:
        print()
        print()
        print("⚠ Wrong Password ⚠")
        print()
        print()
        entry() 
    
    table_create()
     


#######################################################




# ENDING OF PROGRAM 
def exitdes():
    time.sleep(2)
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print("                       ✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠  【E】 【N】 【D】  ✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠")
    print()
    print()
    print()
    print("✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧✧─── ･ ｡ﾟ★: *.✦ .* :★. ───✧")
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    sys.exit()

###################### 




# MAIN


entry()
exitdes()


###############
