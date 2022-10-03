while(True):
    print("""
Temperature Conversions     
    Enter 1 to convert Celsius to Fahrenheit
    Enter 2 to convert Fahrenheit to Celsius
    Enter 3 to convert Celsius to Kelvin
    Enter 4 to convert Kelvin to Celsius
    Enter 5 to convert Fahrenheit to Kelvin
    Enter 6 to convert Kelvin to Fahrenheit
    Enter 7 to quit""")

    a = int(input("Enter your choice of conversion: "))
    if a == 1:
        c = float(input("Enter the temperature in Celsius: "))
        f = (c * 9/5) + 32
        print("The temperature in Fahrenheit is: ", f)
    elif a == 2:
        f = float(input("Enter the temperature in Fahrenheit: "))
        c = (f - 32) * 5/9
        print("The temperature in Celsius is: ", c)
    elif a == 3:
        c = float(input("Enter the temperature in Celsius: "))
        k = c + 273.15
        print("The temperature in Kelvin is: ", k)
    elif a == 4:
        k = float(input("Enter the temperature in Kelvin: "))
        c = k - 273.15
        print("The temperature in Celsius is: ", c)
    elif a == 5:
        f = float(input("Enter the temperature in Fahrenheit: "))
        k = (f - 32) * 5/9 + 273.15
        print("The temperature in Kelvin is: ", k)
    elif a == 6:
        k = float(input("Enter the temperature in Kelvin: "))
        f = (k - 273.15) * 9/5 + 32
        print("The temperature in Fahrenheit is: ", f)
    elif a == 7:
        break
    else:
        print("Invalid choice")