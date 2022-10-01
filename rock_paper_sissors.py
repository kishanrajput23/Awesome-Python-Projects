import random
def gamewin(comp,you):
  if comp==you:
    return None
  elif comp == 'r':
    if you=='p':
      return True
    if you=='s':
      return False
  elif comp =='p':
    if you=='s':
      return True 
    if you=='r':
      return False
  elif comp=='s':
    if you=='r':
      return True
    if you=='p':
      return False
randNo = random.randint(1,3)

print("computer's turn: rock(r) paper(p) or sissors(s)?")
if randNo==1:
   comp='r'
elif randNo==2:
   comp='p'
elif randNo==3:
   comp='s'
 
you=input("your turn: rock(r) paper(p) or sissors(s)?")
a=gamewin(comp,you)
print(f"computer choose {comp}")
print(f"you choose {you}")
if a==None:
  print("it's a tie")
elif a:
  print("you win")
else:
  print("computer won")
