# 1. Using loops
def merge1(l1,l2):
    l3=[]
    for i in l1:
        if i not in l2:
            l3.append(i)
    print(l3)

# 2. Using Sets
def merge2(l1,l2):
    l4=list(set(l1+l2))
    print(l4)

# 3. Using numpy module
def merge3(l1,l2):
    import numpy as np
    res = np.unique(l1 + l2)
    print(res)

def creating_list():
    l1=[]
    l2=[]
    l=int(input("Enter number of list elements: "))
    for i in range(0,l):
        element1=int(input())
        l1.append(element1)
    k=int(input("Enter number of list elements: "))
    for i in range(0,k):
        element=int(input())
        l2.append(element)