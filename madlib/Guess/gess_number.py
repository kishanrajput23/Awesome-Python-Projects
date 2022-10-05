import random

def guess(x):
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f'Guess a number between 1 and {x}: '))
        if guess<random_number:
            print('sorry, guesss again, too low!')

        elif guess>random_number:
            print('sorry! guess again, too high! ')

    print(f'yayyyy!you guessed the number {guess} correctly!')
guess(10)

