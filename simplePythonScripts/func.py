   #user define function called student with parameters
def student(name,age,*marks):         #the * on marks makes it a tuple meanin can take multiple elements
    print('name:', name)
    print('age:', age)

    print('chemistry:\t',marks[0], '\nbiology:\t',marks[1],'\nphysic:\t\t', marks[2])
student('Miami', 25, 70, 55, 63)
print("------------------------------")

print(student('mamo',20,58,45,96))
print("------------------------------")

    #function with parameter and double ** on sales
def bus_owner(user_name, shop_name, **products):
    print("Enter Username: ", user_name)
    print("Enter shop_name: ",shop_name)
    for keys, values in products.items():
        print(keys, ': FCFA',values)
bus_owner('Hyacinth', 'ElectronicShop', API=25100, itel550=55000, televisionV5=101500)
