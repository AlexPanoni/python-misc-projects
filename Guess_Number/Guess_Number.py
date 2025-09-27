from random import randint
from time import sleep
import os
new = ' '

while True:
    if new in 'Nn':
        break
    os.system('cls' if os.name == 'nt' else 'clear')

    print('='*20, 'GUESS THE NUMBER ', '='*20)
    print()
    print('''I've just thought of a number between \033[34m1\033[m and \033[34m100\033[m. 
Let's see how many guesses it takes for you to find it!''')
    print()
    num = randint(1, 100)
    tries = 0
    guesses = []
    while True:
        try:
            guess = int(input('Your guess: '))
            if 0 > guess or guess > 100:
                print('\033[31mBetween 1 and 100, please.\033[m')
                print()
                continue
            elif guess in guesses:
                print('\033[34mYou\'ve already guessed this number!\033[m')
                print()
                continue
        except:
            print('\033[31mInvalid option. Guess a whole number between 1 and 100.\033[m')
            print()
            continue
        tries +=1
        guesses.append(guess)
        if guess == num:
            break
        if num > guess:
            print(f'\033[32mIt\'s more than {guess}!\033[m')
            print()
        if num < guess:
            print(f'\033[33mIt\'s less than {guess}!\033[m')
            print()
    print()
    print(f'You got it, the number was \033[34m{num}\033[m. It took you \033[35m{tries}\033[m', 'try. Amazing!' if tries == 1 else 'tries.')
    if tries > 1:
        print(f'Your guesses: {guesses}')
    print()
    while True:
        new = input('Play again? [Y/N] ').strip()[0]
        if new not in 'YyNn':
            print('\033[31mInvalid option. Try again.\033[m')
        else:
            break
print()
sleep(0.3)
print('\033[32m>>>> Finalizando...\033[m')
sleep(0.8)
print('Thanks for playing! Created by Alex PF in 12/20/2024.')
print()