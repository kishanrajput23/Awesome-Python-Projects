#Password-Generator of your choice
print('''
Greetings, this is a password generator😊
''')#Greetings message  
length = int(input("Enter the length of password: ")) #Length of password
print('''
1. characters
2. numbers
3. symbols
4. characters and numbers
5. characters and symbols
6. numbers and symbols
7. characters, numbers and symbols
''')    #What you want your password to contain
contains = input("Enter the type of password you want: ")


import random
import string

#Password-Generator of your choice
if contains == "1" or contains == "2" or contains == "3" or contains == "4" or contains == "5" or contains == "6" or contains == "7":
    if contains == "1" or contains == "characters":
        chars = string.ascii_letters
    elif contains == "2" or contains == "numbers":
        chars = string.digits
    elif contains == "3" or contains == "symbols":
        chars = '~!@#$%^&*()_+=-`~[]{}|;:,./<>?'
    elif contains == "4" or contains == "characters":
        chars = string.ascii_letters + string.digits
    elif contains == "5" or contains == "characters and symbols":
        chars = string.ascii_letters + '~!@#$%^&*()_+=-`~[]{}|;:,./<>?'
    elif contains == "6" or contains == "numbers and symbols":
        chars = string.digits + '~!@#$%^&*()_+=-`~[]{}|;:,./<>?'
    else:
        chars = string.ascii_letters + string.digits + '~!@#$%^&*()_+=-`~[]{}|;:,./<>?'
else:
    print("Invalid input")
    exit()

password = '' #Empty string
for c in range(length):         #Looping through the length of password
    password += random.choice(chars)
print(password)#Printing the password

print("Thanks for using my password generator 👋")#Thank you message
