# завернуть задание home_work_3_2 в вечный цикл

while True:
    age = input('введите возраст: ')
    name = input('введите имя: ')
    if not (age.isdigit()):
        print('Ошибка: повторите ввод')
    elif age.isdigit():
        age = int(age)
        if age <= 0:
            print('Ошибка: повторите ввод')
        elif 0 < age < 10:
            print(f'Привет, шкет {name}')
        elif 10 <= age <= 18:
            print(f'Как жизнь {name}?')
        elif 18 < age < 100:
            print(f'Что желаете {name}?')
        else:
            print(f'{name}, вы лжете - в наше время столько не живут...')
