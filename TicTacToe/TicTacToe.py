import os
os.system('cls')
import random
from time import sleep

plays = 0
turn = 0
new = ' '
player = 0
pc = 0
ties = 0
begin = 0
grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

def game():
    os.system('cls')
    header()
    score()
    print()
    print('                  1     2     3')
    print()
    print('          1      ', grid[0][0], ' | ', grid[0][1], ' | ', grid[0][2])
    print('               ', '-'*17)
    print('          2      ', grid[1][0], ' | ', grid[1][1], ' | ', grid[1][2])
    print('               ', '-'*17)
    print('          3      ', grid[2][0], ' | ', grid[2][1], ' | ', grid[2][2])
    print()
    print()

def check():
    global player
    global pc
    global ties
    if (
    grid[0][0] == grid[0][1] == grid[0][2] != ' '
    or grid[1][0] == grid[1][1] == grid[1][2] != ' '
    or grid[2][0] == grid[2][1] == grid[2][2] != ' '
    or grid[0][0] == grid[1][0] == grid[2][0] != ' '
    or grid[0][1] == grid[1][1] == grid[2][1] != ' '
    or grid[0][2] == grid[1][2] == grid[2][2] != ' '
    or grid[0][0] == grid[1][1] == grid[2][2] != ' '
    or grid[0][2] == grid[1][1] == grid[2][0] != ' '
        ):
        if turn % 2 == 1:
            player += 1
            game()
            print('\033[32mYou win! Congratulations!\033[m')
            print()
        else:
            pc += 1
            game()
            print('\033[31mYou lose! Better luck next time.\033[m')
            print()
        return True

def score():
    print('\033[1mSCORE\033[m')
    print('-'*20 + '¬')
    print(f'{nome}' + '.'*(15 - len(nome)) + f':  \033[34m{player}\033[m')
    print(f'Computer.......:  \033[32m{pc}\033[m')
    print(f'Ties...........:  \033[33m{ties}\033[m')
    print('-'*21)

def clean():
    global grid
    global turn
    global plays
    grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    turn = 0
    plays = 0

def header():
    print('='*15 + '  # TIC TAC TOE #  ' + '='*15)
    print()

header()
while True:
    nome = input('What\'s your name? ')
    if len(nome) > 17:
        print('Your name is too long! Can you give me a nickname?')
    else:
        break


while True:
    if new in 'Nn':
        break
    else:
        clean()
    while True:
        if plays >= 9 and not check():
            print('\033[33mWe tied!\033[m')
            print()
            ties += 1
            break
        if begin % 2 == 0:
            game()
            print('Your play: ')
            while True:
                while True:
                    try:
                        l = int(input('Row: '))
                        c = int(input('Column: '))
                    except:
                        print('\033[31mPlease, use integers only.\033[m')
                    else:
                        if l < 1 or l > 3 or c < 1 or c > 3:
                            print('\033[31mInvalid space. Try again.\033[m')
                        else:
                            break
                if grid[l-1][c-1] == ' ':
                    grid[l-1][c-1] = '\033[34mX\033[m'
                    break
                else:
                    print('\033[31mInvalid play. This space has been already marked.\033[m')
            plays += 1
            turn += 1
        else:
            begin += 1
            turn += 1
        game()
        if check():
            break
        while plays < 9:
            com_l = random.randint(1, 3)
            com_c = random.randint(1, 3)
            if grid[com_l-1][com_c-1] == ' ':
                grid[com_l-1][com_c-1] = '\033[31mO\033[m'
                break
        plays += 1
        turn += 1
        sleep(1)
        game()
        if check():
            break

    while True:
        new = input('Do you want to play again? [Y/N] ').strip()[0]
        if new not in 'YyNn':
            print('Invalid option.')
        else:
            if (player + pc + ties) % 2 != 0:
                begin += 1
            break
            
os.system('cls')
header()
score()
print()
sleep(1)
print('\033[32m>>>> Game over. Thanks for playing.\033[m')
print()