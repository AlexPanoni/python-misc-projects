from time import sleep
import os

portifolio = []
dict = {}
cars = ['Chevrolet Tracker', 'Chevrolet Onix', 'Chevrolet Spin', 'Hyundai HB20', 'Hyundai Tucson', 'Fiat Uno',
          'Fiat Mobi', 'Fiat Pulse']
prices = [120, 90, 150, 85, 120, 60, 70, 130]
rented = []
m = ' '
n = ' '
for i in range(0, 8):
    dict['key'] = int(i)
    dict['car'] = cars[i]
    dict['price'] = int(prices[i])
    portifolio.append(dict.copy())
    dict.clear()

while True:
    if m == '0':
        break
    os.system('cls')
    print('=' * 40)
    print(f'\033[1;33m{"Welcome to Auto Rent!":^40}\033[m')
    print('=' * 40)
    print()
    print('\033[1;32m>>> What do you want to do?\033[m')
    print(
        '\033[34m1\033[m - Show Portfolio  |  \033[34m2\033[m - Rent a Car  !  \033[34m3\033[m - '
        'Return a Car  |  \033[34m0\033[m - End')
    while True:
        n = input('Option: ')
        if n not in '1230':
            print('\033[31mInvalid Option! Try again.\033[m')
        else:
            break
    if n == '0':
        break
    if n == '1':
        os.system('cls')
        for c in range(len(portifolio)):
            print(f'[\033[34m{c + 1}\033[m] {portifolio[c]["car"]} - $ \033[32m{portifolio[c]["price"]}\033[m / day')
        print()
        print('=' * 30)
        print('1 - Back   //  0 - End program')
        while True:
            m = input()
            if m not in '01':
                print('\033[31mInvalid Option! Try again.\033[m')
            else:
                break

    if n == '2':
        while True:
            os.system('cls')
            print('[RENT] Take a look at our portfolio.')
            print()
            for c in range(len(portifolio)):
                print(
                    f'[\033[34m{c + 1}\033[m] {portifolio[c]["car"]} - $ \033[32m{portifolio[c]["price"]}\033[m / day')
            print()
            print('=' * 30)
            while True:
                e = input('Choose the car code (or type \033[34m0\033[m to go Back): ')
                if e not in '012345678':
                    print('\033[31mInvalid Option! Try again.\033[m')
                else:
                    e = int(e)
                    break
            if e == 0:
                break
            else:
                while True:
                    days = input('How many days would you like to rent for? ')
                    if not days.isnumeric():
                        print('\033[31mInvalid value! The number of days must be a whole number.\033[m')
                    else:
                        d = int(days)
                        break
            os.system('cls')
            print(f'You chose \033[35m{portifolio[e - 1]["car"]}\033[m for \033[33m{d}\033[m days.')
            print(
                f'The rental will total \033[32m$ {portifolio[e - 1]["price"] * d}\033[m. Do you want to confirm the rental?')
            print()
            while True:
                print('1 - CONFIRM   //   2 - CANCEL')
                conf = input()
                if conf not in '12':
                    print('\033[31mInvalid Option! Try again.\033[m')
                else:
                    break
            if conf == '1':
                print(f'Congratulations! You rented the {portifolio[e - 1]["car"]} for {d} days. ')
                rented.append(portifolio[e - 1].copy())
                portifolio.pop(e - 1)
            else:
                print('You canceled the rental.')
            print()
            print('=' * 30)
            print('1 - Back   //  0 - End program')
            while True:
                m = input()
                if m not in '01':
                    print('\033[31mInvalid Option! Try again.\033[m')
                else:
                    break
            break

    if n == '3':
        while True:
            os.system('cls')
            print('Here is the list of rented cars. Which one would you like to return? ')
            print()
            if len(rented) == 0:
                print('There are no rented cars at the moment.')
            for a in range(len(rented)):
                print(f'[\033[34m{a + 1}\033[m] {rented[a]["car"]} - $ \033[32m{rented[a]["price"]}\033[m / day')
            print()
            print('=' * 30)
            print('Enter the option code (or type \033[34m0\033[m to go Back):')
            while True:
                o = input()
                if not o.isnumeric():
                    print('\033[31mInvalid option! Try again.\033[m')
                else:
                    if int(o) > len(rented):
                        print('\033[31mInvalid Option! Try again.\033[m')
                    else:
                        o = int(o)
                        break
            if o == 0:
                break
            else:
                print(f'{rented[o - 1]["car"]} returned successfully. ')
                portifolio.append(rented[o - 1].copy())
                portifolio.sort(key=lambda x: x['key'])
                rented.pop(o - 1)
            print()
            print('=' * 30)
            print('1 - Back   //  0 - End program')
            while True:
                m = input()
                if m not in '01':
                    print('\033[31mInvalid Option! Try again.\033[m')
                else:
                    break
            break

sleep(0.5)
print()
print('\033[32m>>Closing program...\033[m')
sleep(1)
print('=' * 30)
print('Thank you and come back anytime!')
print()
