import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
total_people = len(names)
person = random.randint(0, total_people - 1)
print(f"{names[person]} is going to buy the meal today!")
