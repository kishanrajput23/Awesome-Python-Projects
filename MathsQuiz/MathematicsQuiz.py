def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Mathamatics Quiz")
guess1 = input("45+45+45+45 = ?\n Type your Ans. = ")
check_guess(guess1, "180")
guess2 = input("\n1234+0+1.23+98 = ?\n Type your Ans. = ")
check_guess(guess2, "1333.23")
guess3 = input("\n35x12x0-69+69 = ?\n Type your Ans. = ")
check_guess(guess3, "0")
print("\nYour Score is "+ str(score))