# Введите число. Если это число делится на 1000 без остатка, то выведите на экран 'milennium'

number = int(input('введите число: '))
if number % 1000 == 0:
    print('milennium')
