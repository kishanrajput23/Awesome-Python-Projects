class ListIterator:
    def __init__(self, a):
        self.__list = a
        self.__index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.__index +=1
        return self.__list[self.__index]

a = [2, 3, 6, 8, 5, 4]
mylist = ListIterator(a)
it = iter(mylist)
print(it)
print(next(it))