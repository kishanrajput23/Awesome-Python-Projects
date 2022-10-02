    #variables
x = 15                        #interger type

y = 5.3                      #float type
z = 3.0

first_name = "Miami"         #string type
second_name = "miamo yoaleu"
last_name = "HYACINTH"

   #converting a float y to interger and storing the values in another variable i
i = int(y)
print(i)      #print the value of i and get the different between i and y

    #converting an interger x to a float and storing the values in another variable j
j = float(x)
print(j)      #print the value of j and get the different between j and x

   #multiplication of variable x and y and print the result
print("{0} * {1} = {2}".format(x,y,x*y))

    #capitilize the content of the variable second_name
print(second_name.capitalize())

    #variable first_name is printed in uppercase letter
print(first_name.upper())

    #variable last_name is printed in lowercase letter
print(last_name.lower())

    #check if variable first_name is uppercase and answer is in boolean
print(first_name.isupper())

    #print a statement with multiple datatype
print("Mr. %s are you %d years old? " %(first_name,x), "\n\tWhy ask?")