import random
no=random.randint(1,3)
if no==1:
    Player1='s'
elif no==2:
    Player1='w'
else:
    Player1='g'
Player2=input("Player2:Snake(s) or water(w) or gun(g):")
print("Player1:Snake(s) or water(w) or gun(g):",Player1)
def gameresult(Player1,Player2):
    if Player1==Player2:
        return None
    elif Player1=='s':
        if Player2=='w':
            return False
        elif Player2=="g":
            return True
    elif Player1=='w':
        if Player2=='g':
            return False
        elif Player2=="s":
            return True
    elif Player1=='g':
        if Player2=='s':
            return False
        elif Player2=="w":
            return True
result=gameresult(Player1,Player2)
if result==None:
    print("It'a a tie")
elif result==True:
    print("You Win")
else:
    print("You Lost")
