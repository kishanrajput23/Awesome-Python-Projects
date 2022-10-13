# define the input
def solve(n):
   for i in range(n-1,-1,-1):
      for j in range(i):
         print(end="--")
      for j in range(n-1,i,-1):
         print(chr(j+97),end="-")
      for j in range(i,n):
         if j != n-1:
            print(chr(j+97),end="-")
         else:
            print(chr(j+97),end="")
      for j in range(2*i):
         print(end="-")
      print()
   for i in range(1,n):
      for j in range(i):
         print(end="--")
      for j in range(n-1,i,-1):
         print(chr(j+97),end="-")
      for j in range(i,n):
         if j != n-1:
            print(chr(j+97),end="-")
         else:
            print(chr(j+97),end="")
      for j in range(2*i):
         print(end="-")
   print()

n = 8
solve(n)

##For testing purpose only
##You can change 'n' value to get different output

#Input = 8

#Output: 

#    --------------h--------------
#   ------------h-g-h------------
#    ----------h-g-f-g-h----------
#    --------h-g-f-e-f-g-h--------
#    ------h-g-f-e-d-e-f-g-h------
#    ----h-g-f-e-d-c-d-e-f-g-h----
#    --h-g-f-e-d-c-b-c-d-e-f-g-h--
#    h-g-f-e-d-c-b-a-b-c-d-e-f-g-h
#    --h-g-f-e-d-c-b-c-d-e-f-g-h--
#    ----h-g-f-e-d-c-d-e-f-g-h----
#    ------h-g-f-e-d-e-f-g-h------
#    --------h-g-f-e-f-g-h--------
#    ----------h-g-f-g-h----------
#    ------------h-g-h------------
#    --------------h--------------
