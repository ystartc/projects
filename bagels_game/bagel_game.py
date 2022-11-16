#!/usr/bin/env python3
import random

print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a N-digit number (later you will input desired N value) with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:
Pico
Fermi
Bagels
That means:
One digit is correct but in the wrong position.
One digit is correct and in the right position.
No digit is correct.''')

MAX_GUESSES = int(input('> The maximum number of guesses: '))
NUM_DIGITS = int(input('> The lenght of the guessed number (N): '))


def main():

    secret_number = sec_num()
    #print(secret_number)

    num_guesses = 1
    while num_guesses <= MAX_GUESSES:
        guess = input('Your guess: ')

        if not guess.isdecimal() or len(guess) != len(secret_number):
            print('Incorrect input! Please enter {} digit characters. Try again...'.format(len(secret_number)))
            continue

        if guess == secret_number:
            print('Congratulations! You got it! The number {} you guessed is a secret number.'.format(guess))
            break

        if num_guesses < MAX_GUESSES:
            print('Sorry! Wrong number.Try again...')
            print(hints(guess, secret_number))
            print('Guesses left: ', MAX_GUESSES-num_guesses)
            num_guesses += 1

        else:
            num_guesses += 1
            print('Game over! You out of guesses. You lost. The guessed number was: {}.'.format(secret_number))


def sec_num():
    #secret_number = ''.join(str(random.randint(0, 9)) for _ in range(NUM_DIGITS))
    numb = range(0, 9)
    s_n_list = random.sample(numb, NUM_DIGITS)
    secret_number = ''.join(str(n) for n in s_n_list)
    return secret_number

def hints(guess, secret_number):
    hint = []

    for i in range(len(secret_number)):
        if guess[i] in secret_number:
            if guess[i] == secret_number[i]:
                hint.append('Fermi')
            else:
                hint.append('Pico')

    if not hint:
        hint.append('Bagels')

    hint.sort()
    return hint

if __name__ == '__main__':
    main()
    #print(hints('158', '318'))
