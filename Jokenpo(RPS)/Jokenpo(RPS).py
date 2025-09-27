import random
from time import sleep
from emoji import emojize
import os

human = 0
comp = 0
draw = 0
a = ' '

def cabeçalho():
    print('='*100)
    print(f'\033[1;33m{emojize(":raised_fist::raised_hand::victory_hand: ") + "  JO-KEN-PO  " + emojize(":raised_fist::raised_hand::victory_hand: "):^100}\033[m')
    print('='*100)
    print()

def placar():
    print()
    print('-'*15 + '¬')
    print('\033[1mSCORE: \033[m')
    print(f' {name}: \033[32m{human}\033[m')
    print(f' Computer: \033[31m{comp}\033[m')
    print(f' Ties: \033[33m{draw}\033[m')
    print()

os.system('cls')
cabeçalho()
print('\033[32m>>> Let’s play Rock, Paper & Scissors, the classic \033[34mShowdown of Champions\033[32m!\033[m')
print()
name = input('Type your name or nickname: ')

while True:
    if a == '0':
        break
    os.system('cls')
    cabeçalho()
    print('\033[32m>>> Let’s play Rock, Paper & Scissors, the classic \033[34mShowdown of Champions\033[32m!\033[m')
    placar()
    print('=-'*50)
    print('''Type:
        \033[34m1\033[m - to PLAY   |   \033[34m2\033[m - to SEE THE RULES   |   \033[34m0\033[m - to Quit the Game''')

    while True:
        opt = input()
        if opt != '1' and opt != '2' and opt != '0':
            print('\033[31mInvalid option! Try again.\033[m')
        else:
            break

    if opt == '1':
        while True:
            os.system('cls')
            cabeçalho()
            print()
            placar()
            print('=-'*50)
            print(emojize('''Make your move:
        Type \033[1;32m1\033[m to pick Rock :raised_fist: //  Type \033[1;32m2\033[m to pick Paper :raised_hand: //  Type \033[1;32m3\033[m to pick Scissors :victory_hand:
        '''))
            while True:
                j = input()
                if j != '1' and j != '2' and j != '3':
                    print(emojize('You picked an \033[1;31minvalid option\033[m!:horse_face: Try again.'))
                else:
                    j = int(j)
                    break
            print()
            sleep(0.5)
            print('JO')
            sleep(0.5)
            print('KEN')
            sleep(0.5)
            print('''PO!!!
            ''')
            sleep(1)
            l = ['Rock', 'Paper', 'Scissors']
            m = random.choice(l)

            print('=' * 25)
            if j == 1:
                print(name + ' ')
                print(emojize('          :raised_fist:'))
            elif j == 2:
                print(name + ' ')
                print(emojize('          :raised_hand:'))
            elif j == 3:
                print(name + ' ')
                print(emojize('          :victory_hand:'))
            if m == 'Rock':
                print(emojize('''           x 
          :raised_fist:'''))
                print('                Computer')
            elif m == 'Paper':
                print(emojize('''           x 
          :raised_hand:'''))
                print('                Computer')
            elif m == 'Scissors':
                print(emojize('''           x
          :victory_hand:'''))
                print('                Computer')
            print('=' * 25 + '''
            ''')



            if j == 1 and m == 'Rock':
                print(emojize('''You picked \033[1;34m"Rock"\033[m :raised_fist: and I also picked \033[1;31m"Rock"\033[m :raised_fist:. 
                
                \033[1;36mIt’s a tie!\033[m Wanna go again?'''))
                draw += 1
            elif j == 1 and m == 'Paper':
                print(emojize('''You picked \033[1;34m"Rock"\033[m :raised_fist: and I picked \033[1;31m"Paper"\033[m :raised_hand:. 
                
                \033[1;31mI win!\033[m Bow before the champion!! :smiling_face_with_sunglasses:'''))
                comp += 1
            elif j == 1 and m == 'Scissors':
                print(emojize('''You picked \033[1;34m"Rock"\033[m :raised_fist: and I picked \033[1;31m"Scissors"\033[m :victory_hand:. 
                
                \033[1;32mCongrats, you won!\033[m I bet you cheated... :unamused_face:'''))
                human += 1
            elif j == 2 and m == 'Rock':
                print(emojize('''You picked \033[1;34m"Paper"\033[m :raised_hand: and I picked \033[1;31m"Rock"\033[m :raised_fist:. 
                
                \033[1;32mCongrats, you won!\033[m I bet you cheated... :unamused_face:'''))
                human += 1
            elif j == 2 and m == 'Paper':
                print(emojize('''You picked \033[1;34m"Paper"\033[m :raised_hand: and I also picked \033[1;31m"Paper"\033[m :raised_hand:. 
                
                \033[1;36mIt’s a tie!\033[m Wanna go again?'''))
                draw += 1
            elif j == 2 and m == 'Scissors':
                print(emojize('''You picked \033[1;34m"Paper"\033[m :raised_hand: and I picked \033[1;31m"Scissors"\033[m :victory_hand:. 
                
                \033[1;31mI win!\033[m Bow before the champion!! :smiling_face_with_sunglasses:'''))
                comp += 1
            elif j == 3 and m == 'Rock':
                print(emojize('''You picked \033[1;34m"Scissors"\033[m :victory_hand:  and I picked \033[1;31m"Rock"\033[m :raised_fist:. 
                
                \033[1;31mI win!\033[m Bow before the champion!! :smiling_face_with_sunglasses:'''))
                comp += 1
            elif j == 3 and m == 'Paper':
                print(emojize('''You picked \033[1;34m"Scissors"\033[m :victory_hand:  and I picked \033[1;31m"Paper"\033[m :raised_hand:. 
                
                \033[1;32mCongrats, you won!\033[m I bet you cheated... :unamused_face:'''))
                human += 1
            elif j == 3 and m == 'Scissors':
                print(emojize('''You picked \033[1;34m"Scissors"\033[m :victory_hand:  and I also picked \033[1;31m"Scissors"\033[m :victory_hand:. 
                
                \033[1;36mIt’s a tie!\033[m Wanna go again?'''))
                draw += 1
            else:
                print(emojize('You picked an \033[1;31minvalid option\033[m!:horse_face: Try again.'))
            print()
            print('=-'*50)
            print('1 - PLAY AGAIN    |     2 - BACK    !    0 - END PROGRAM')
            while True:
                a = input()
                if a != '0' and a != '1' and a != '2':
                    print(emojize('You picked an \033[1;31minvalid option\033[m!:horse_face: Try again.'))
                else:
                    break
            if a == '2' or a == '0':
                break
    if opt == '2':
        while True:
            os.system('cls')
            cabeçalho()
            print('''
            \033[1mThe rules are simple:\033[m 
            \033[33m 
            I’ll pick one option: Rock, Paper, or Scissors.  
            You’ll do the same.  
            Then we compare our choices.  
            Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.  
            If we pick the same, it’s a tie!\033[m
            ''')
            print('''Ready to play?
            ''')
            input('Press any key to go back: ')
            break

    if opt == '0':
        break

os.system('cls')
cabeçalho()
print()
placar()
print('=-'*40)
sleep(0.5)
print('\033[32m>>>>>> Closing the game...\033[m')
sleep(1)
print()
print('Thanks for playing! See you next time.')
print()
print('>>> Developed by Alex PF on 05/12/2024.')
print('''
          
       
      ''')