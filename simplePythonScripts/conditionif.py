print("Grade List")
print("==========")

#You have to take the marks of the student as input from the user.
# Then assign the grades based on marks obtained by the students.
def gradeAssign(marks):
    assert marks >= 0 and marks <= 100

    if marks >= 90:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    return grade


def main():
    marks = float(input('Enter your marks: '))
    print("Marks: ", marks, "\nGrade: ", gradeAssign(marks))

main()

print("======================================================")

#Python Code To Check If The Year Is A Leap Year
#The year 2000 was a leap year, for example, but the years 1700, 1800, and 1900 were not
def checkYear(year):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print(year, ' is a leap year')
    else:
        print(year, ' is not a leap year')


def main():
    year = int(input('Enter the number of rows: '))
    checkYear(year)


main()

print("======================================================")
print("Find the maximum Number")
print("==========")


def FindMaximum(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            maxNumber = n1
        else:
            maxNumber = n3
    elif n2 > n3:
        maxNumber = n2
    else:
        maxNumber = n3
    return maxNumber


def main():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter Second numer: "))
    n3 = int(input("Enter Third number: "))

    maximum = FindMaximum(n1, n2, n3)
    print("Maximum number is", maximum)