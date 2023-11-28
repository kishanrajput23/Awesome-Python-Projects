# Love Calculator using the count function

print("Welcome to the Love Calculator!")

# Input user's name
name1 = input("What is your name? \n")

# Input partner's name
name2 = input("What is their name? \n")
name3 = (name1 + name2).lower()


T = name3.count("t") 
R = name3.count("r")
U = name3.count("u")
E = name3.count("e")
L = name3.count("l")
O = name3.count("o")
V = name3.count("v")
E = name3.count("e")
is_true = T + R + U + E 
is_love = L + O + V + E 

# calculating the total score
love_score = int(str(is_true) + str(is_love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score < 50 and love_score > 40:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")