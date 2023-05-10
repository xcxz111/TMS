# Сделать программу в которой нужно будет угадывать число.

from random import randint

print('Привет, это игра в которой нужно угадать число \n')


def menu():
    choice_menu = input(f'Введите 1 - что бы начать \nВведите 2 - что бы посмотреть статистику \n\nВаш выбор: ')
    if choice_menu == '1':
        lev()
    elif choice_menu == '2':
        print('статистика находится на стадии разработки \n')
        menu()
    else:
        print('вы ввели что то не корректное \n')
        menu()


def lev():
    print(f'Выберите сложность\n')
    level = input(f'Введите 1 - легко \nВведите 2 - средне \nВведите 3 - сложно \nВведите 4 - своя игра \nВаш выбор: ')
    if level == '1':
        game(3, 2)
    elif level == '2':
        game(10, 5)
    elif level == '3':
        game(100, 20)
    elif level == '4':
        lot = input('введите количество загаданных чисел')
        life = input('введите количество жизней')
        game(lot, life)
    else:
        print('вы ввели что то не корректное')
        lev()


def game(lot, life):
    x = randint(1, lot)
    print(f'компьютер загадал число от 1 до {lot} у вас {life} попыток \nчто бы покинуть игру введите: 000')
    guess(x, life)
    return x


def guess(x, life):
    loop = 1
    while True:
        n = input('Введите загаданное число: ')
        if n.isdigit():
            n = int(n)
            if n == x:
                print(f'\n \nПоздравляем!!! вы угадали число c {loop} раза!!! \nхотите сыграть еще?')
                win()
            elif n < x:
                life -= 1
                loop += 1
                print(f'\nне верно, загаданное число больше... у вас осталось {life} попыток')
            elif n > x:
                print(f'\nне верно, загаданное число меньше...у вас осталось {life} попыток')
                loop += 1
        elif not n.isdigit():
            print('Ошибка: введите число')
            guess(x, life)
        if life == 0:
            print('вы проиграли!')
            win()


def win():
    more = input(
        'Введите + что бы начать новую игру' + '\n' + 'Введите - что бы вернуться в меню' + '\n' + 'Ваш выбор: ')
    if more == '+':
        lev()
    elif more == '-':
        menu()
    else:
        print('\n' + 'вы ввели что то не корректное' '\n')
        win()


menu()
