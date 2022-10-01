# computer random guess number
# user guess random number
# if user > computer then number is smaller
# if user < computer then number is greater
# if user == computer you guess number in 10 attempt

import random

print("\nComputer guess the number...")
computer = random.randrange(100)
# print(computer)

user = int(input("\nUser guess the number(Upto 100)... "))


def ran_number(computer, user, count=1):

    if user < 100:
        if user < computer:
            user = int(input("Please choose number bigger "))
            count += 1
            ran_number(computer, user,count)

        elif user > computer:
            user = int(input("Please choose number smaller "))
            count +=1
            ran_number(computer, user,count)

        else:
            print(f"\n Congrates! You guess the number in {count} attempt")

    else:
        print("\n\nNumber range must be under ......")


ran_number(computer, user)
print(f"\nComputer was choosed {computer}")


