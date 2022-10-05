    #User enter an interger value
num= int(input("Enter number : \n"))
    #condition check if number enterred id zero or not
if num != 0:
    if num>0:                                     #condition check if number is greater than zero
        if num %2 ==0:                            #condition check if number is greater is divisible by two or not
            print("Number is positive even ")
        else:
            print("Number is a positive odd ")
    else:
        if num%2 == 0:
            print("Number is a Negative even")
        else:
            print("Number is a Negative odd")

else:
    print("number is Zero")