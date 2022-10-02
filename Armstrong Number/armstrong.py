# An Armstrong number of three digits is an integer such that the sum of the cubes of its digits is equal to the number itself. 
# Ex : 371 is an Armstrong number since 3**3 + 7**3 + 1**3 = 371.

n = str(input("Enter Number: "))
s = 0
for i in n:
    s = s + int(i)**3
if(s == int(n)):
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")
