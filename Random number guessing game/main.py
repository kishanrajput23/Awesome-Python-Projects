import random
def Guess(a,b,actual):
    guess=int(input(f"PLEASE ENTER A NUMBER BETWEEN {a} AND {b}\n"))
    nguess=0
    while guess!=actual:
        if guess < actual:
            guess=int(input("PLEASE ENTER A HIGHER NUMBER\n"))
            nguess+=1
        else:
            guess=int(input("PLEASE ENTER A SMALLER NUMEBR\n"))
            nguess+=1
    print(f"you guessed the number in {nguess} guess")
    return nguess
if __name__== "__main__":
    a=int(input("PLEASE ENTER THE VALUE OF A\n"))
    b=int(input("PLEASE ENTER THE VALUE OF B\n"))
    actual1=random.randint(a,b)
    print("PLAYER 1 TURN\n")
    g1=Guess(a,b,actual1)
    print("PLAYER 2 TURN\n")
    actual2=random.randint(a,b)
    g2=Guess(a,b,actual2)
    if g1<g2:
        print("PLAYER 1 WON THE GAME\n")
    elif g2<g1:
        print("PLAYER 2 WON\n")
    else:
        print("IT IS A TIE\n")