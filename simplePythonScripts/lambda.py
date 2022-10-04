def double(x):
    return x*2

def add(x , y):pass
    #return x + y

#lambda will perform this same operation (function) in line 16 and will override this function at line8 when the function is call
def product(x, y, z):
    return x * y * z

#These statments call are functions on their own, they are lambda function which are similar to user define function shown above
doubl = lambda i:i *2

add = lambda x, y : x + y

product = lambda x, y, z: x+y+z


print(doubl(10))
print(add(13, 21))
print(product(10, 11, 13))