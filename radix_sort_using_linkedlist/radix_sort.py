class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:        
    def __init__ (self):
        self.head = None
        self.size = 0
        
    def _format_str (self, val):
        s = str(val) + ' : '
        p = self.head
        for i in range(self.size):
            s += str(p.data) + ' '
            p = p.next
        return s

    def print_l(self, val):
        return self._format_str(val)
    
    def __len__ (self):
        return self.size
    
    def __str__ (self):
        s = ''
        p = self.head
        for i in range(self.size):
            s += str(p.data)
            if i < self.size - 1:
                s += " -> "
            p = p.next
        return s
    
    def isEmpty(self):
        return self.size == 0
    
    def indexOf(self, data):
        p = self.head
        for i in range(len(self)):
            if p.data == data:
                return i
            p = p.next
        return -1
    
    def isIn(self, data):
        return self.indexOf(data) >= 0
    
    def nodeAt(self, i):
        p = self.head
        for j in range(0, i):
            p = p.next
        return p
    
    def insertAfter(self, i, data):
        p = Node(data)
        q = self.nodeAt(i)
        p.next = q.next
        q.next = p
        self.size += 1
        
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.size += 1
        else:
            self.insertAfter(len(self) - 1, data)
            
    def appendWithCompare(self, data):
        p = self.head
        if p != None:
            count = 0
            while data < p.data:
                count += 1
                if p.next != None: 
                    p = p.next
                else: break
            if count == 0:
                self.addHead(data)
            else:
                self.insertAfter(count - 1, data)
        else:
            self.append(data)
            
    def deleteAfter(self, i):
        if self.size > 0:
            q = self.nodeAt(i)
            tmp = q.next
            q.next = q.next.next
            self.size -= 1
            return tmp.data
        
    def delete(self, i):
        if i == 0 and self.size >= 0:
            p = self.head
            self.head = self.head.next
            self.size -= 1
            return p.data
        else:
            return self.deleteAfter(i-1)

    def removeData(self, data):
        if self.isIn(data):
            self.deleteAfter(self.indexOf(data) - 1)
            
    def addHead(self, data):
        if self.isEmpty():
            self.head = Node(data)
            self.size += 1
        else:
            p = self.head
            node = Node(data)
            node.next = p
            self.head = node
            self.size += 1
    
    def sortRail(self):
        i = self.indexOf("0")
        if i > -1:
            for j in range(i):
                l = self.delete(0)
                self.append(l.data)
                
    def deleteHead(self):
        p = self.head
        self.head = p.next
        self.size -= 1
        return p.data
        
    def getMax(self):
        p = self.head
        most = p.data
        for i in range(1, self.size):
            if most < p.next.data:
                most = p.next.data
            p = p.next
        return most
    
    def getMaxDigit(self, val):
        digit = 0
        while(val):
            digit += 1
            val //= 10
        return digit
    
    def isSorted(self):
        p = self.head
        count = 0
        for i in range(self.size - 1):
            if p.data >= p.next.data:
                count += 1
                p = p.next
        return count == self.size - 1
    
def get_index_value(val, index):
    digit = 0
    while(digit < index - 1):
        digit += 1
        val //= 10
    return val % 10

def main():
    inp = input("Enter Input : ").split()
    L = LinkedList()
    L1 = LinkedList()
    loop = 0
    for i in inp:
        L.append(int(i))
        L1.append(int(i))
    max_bits = L.getMaxDigit(L.getMax())
    llist = [LinkedList() for i in range(10)]
    for i in range(1, max_bits + 2):
        while L.size > 0:
            num = L.deleteHead()
            digit_val = get_index_value(abs(num), i)
            llist[digit_val].appendWithCompare(num)
        print("------------------------------------------------------------")
        print("Round : {}".format(i))
        check_first_index = LinkedList()
        for j in range(10):
            print(llist[j].print_l(j))
            while not llist[j].isEmpty():
                val = llist[j].delete(llist[j].size - 1)
                if j == 0:
                    check_first_index.addHead(val)
                L.addHead(val)
        loop += 1
        if L.isSorted() and check_first_index.size == L.size:
            break
    print("------------------------------------------------------------")
    print("{} Time(s)".format(loop - 1))
    print("Before Radix Sort : ", end = "")
    print(L1)
    print("After  Radix Sort : ", end = "")
    print(L)

if __name__ == '__main__':
	main()
