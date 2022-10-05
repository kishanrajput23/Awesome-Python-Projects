    # list : a single variable that can take many values called elements
x= [2, 5, 8, 6, 0]                   #list intergers
y = ['Max', 5, 3.2, [2, 4]]          ##it is possible to save multiple data types values in a list
z = ['Max', 'Jhon', 'peter', 1]

print(y[0])        #print out the value of the first element at first index from the list y

print(y[3])

print(z[2])

        #insert and remove from a list
print(x.insert(2, 'Tome'))           #at position two in the list x, Tom is inserted
print(z.remove('Jhon'))              #Jhon is to be remove from the list z

w = z.copy()                        #this copy the content of z into the list of w


