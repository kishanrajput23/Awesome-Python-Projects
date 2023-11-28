# We have 3 choice for selecting snake, water, function
# we have selected anything from 3 choices
# computer choose randomly among three choices

# if I choose snake and computer choose water then snake win
# if I choose snake and computer choose gun then gun win
# if I choose snake and computer choose snake then match draw

# if I choose gun and computer choose water then water win
# if I choose gun and computer choose water then gun win
# if I choose gun and computer choose water then gun match tie

# if I choose water and computer choose gun then water won
# if I choose water and computer choose snake then snake won
# if I choose water and computer choose water then draw

import random

score = 0
i = 1

while i <= 5:

    computer_guesses = ['snake', 'water', 'gun']
    print(f"{i}. Computer has choose value....")
    compChoice = random.choice(computer_guesses)

    print("Choose any one from snake, water, gun ")
    myChoice = input()

    if myChoice == "snake" or myChoice == "water" or myChoice == "gun":
        if myChoice == 'snake' and compChoice == 'water':
            print("You win!!")
            score += 1
        elif myChoice == 'snake' and compChoice == 'gun':
            print("You lost!!")
        elif myChoice == 'water' and compChoice == 'gun':
            print("You win!!")
            score += 1
        elif myChoice == 'water' and compChoice == 'snake':
            print("You lost!!")
        elif myChoice == 'gun' and compChoice == 'snake':
            print("You win!!")
            score += 1
        elif myChoice == 'gun' and compChoice == 'water':
            print("You lost!!")
        else:
            print("Match draw!!")
        i += 1
    else:
        print("Enter valid input...")
print("\nYour Total score: ", score)
