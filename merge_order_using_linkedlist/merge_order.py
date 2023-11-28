class node:
    def __init__(self,data,next = None ):
        self.data = data
        self.next = next
    def __str__(self):
        return self.data

def createList(l=[]):
    count = 1
    for i in l:
        new_node = node(i)
        if count == 1:
            nodes = new_node
        else:
            tmp = nodes
            while tmp.next:
                tmp = tmp.next 
            tmp.next = new_node
        count += 1 
    return nodes

def printList(H):
    ll = []
    while H:
        ll.append(str(H))
        H = H.next
    print(' '.join(ll))

def mergeOrderesList(p,q):
    count = 1
    while p and q:
        if count == 1:
            if int(str(p)) < int(str(q)):
                merge_nodes = node(str(p))
                p = p.next
            else:
                merge_nodes = node(str(q))
                q = q.next
            head = merge_nodes
        else:
            if int(str(p)) < int(str(q)):
                merge_nodes.next = node(str(p))
                p = p.next
            else:
                merge_nodes.next = node(str(q))
                q = q.next
            merge_nodes = merge_nodes.next
        count += 1

    if p or q:
        merge_nodes.next = p if p else q

    return head

# input only a number save in L1,L2
L1, L2 = input("Enter 2 Lists : ").split()
LL1 = createList(L1.split(','))
LL2 = createList(L2.split(','))
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)