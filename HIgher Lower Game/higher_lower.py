from art import logo,vs
from game_data import data
import random
from os import system
#display art 
print(logo)
score = 0
game_continue = True
account_b = random.choice(data)

def format_data(account):
    """formate the account data into printable format"""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr} from {account_country}"

def answer_checking(guess,a_followers ,b_followers):
    """checks users guess is correct or not"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
while game_continue:
    #Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")


    #ask user for a guess
    guess = input("who has more followers? Type 'A' or 'B': ").lower()


    #check if user is correct
    ## Get folllower count of each account
    a_followers_count  = account_a["follower_count"]
    b_followers_count  = account_b["follower_count"]

    is_correct = answer_checking(guess, a_followers_count,b_followers_count)

    #clear the screen between the rounds
    system("clear")
    print(logo)
    ## use if statement to check if user is correct
    if is_correct:
        score += 1
        print(f"There you are..! it's right 🔥 your current score is {score}")
    else:
        game_continue = False
        print(f"ohh...that's wrong...🥱.. Your final score is {score}")



