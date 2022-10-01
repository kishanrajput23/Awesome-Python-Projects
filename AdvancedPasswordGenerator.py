import string

import random

print("Welcone to Password Generator\n")

forwhat = input("Enter the website or application for which you want to generate password:\n")

length = int(input("Enter the length of password(Max-94)\n"))

if length >= 94:

	print("Max length crossed.") 	quit()

s1 = list(string.ascii_lowercase)

s2 = list(string.ascii_uppercase)

s3 = list(string.digits)

s4 = list(string.punctuation)

elements = s1+s2+s3+s4

random.shuffle(elements)

password = "".join(elements[0:length])

print("The safe generated password is :",password,"\n")

saveyn = input("Do you want save the password?\nEnter Yes or No\n")

if saveyn == "Yes":

	f = open("generatedpasswords.txt","a")

	f.write(forwhat + " - " + password+"\n")

	f.close()

	print("Your password is succesfully saved in 'generatedpasswords.txt' file.")
