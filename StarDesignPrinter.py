print("Welcome to STAR PRINTING Program!\n")

ptype = input("How you want to print?\n 1 for Low to High\n 2 for High to low\n")

n = int(input("How many rows you want to Print?\n"))

if ptype == "2":

	a = n	while a > 0:

		print("*"*a)

		a = a - 1

if ptype == "1":

	a = n

	for j in range(a+1):

		print("*"*j)

		a = a +1

	
