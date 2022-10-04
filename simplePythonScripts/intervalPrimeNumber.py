def prime():
    startNum = int(input("Enter Lowest Number: "))
    endNum = int(input("Enter Highest Number: "))
    for num in range(startNum, endNum + 1):
        if num>1:
            for i in range(2, num):
                if (num%i == 0):
                    break
            else:
                print(num)
prime()
