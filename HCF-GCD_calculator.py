#Author: Vishwajeet Bamane

#Last modified on: 20/09/2020

print("HCF/GCD Calculator\nOnly enter integers\n")

num1 = int(input("Enter the first number: "))

num2 = int(input("Enter the second number: "))

if num1 < num2:

	mx = num1else:

	mx = num2

for i in range(1,mx+1):

	if num1%i==0 and num2%i == 0:

		hcf = i

print(hcf)
