  #tuple are just ad list but differ from list in that, tuples are immutable(cannot be change once created)
x= (1, 5, 3, 7, 5)
y= ('Man', 5, 8, 'Hyacinth')         #it is possible to save multiple data types values in a tuple as list
  #you cannot insert or remove anything from the tuple

print(x.count(5))       # count the number of 5 in the tuple
print(len(y))           # display the number if element found in the tuple
del(y)                  # delete the tuple y