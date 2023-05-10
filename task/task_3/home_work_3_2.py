# Написать программу, которая получит имя и возраст пользователя
# проверяет возраст и выдаёт приветственное сообщение в зависимости от возраста:
# - меньше нуля или ноль или не число:" Ошибка, повторите ввод"
# - больше нуля до 10 не включая: "Привет, шкет #имя#"
# - от 10 до 18 включая: "Как жизнь #имя#? "
# - больше 18 и меньше 100: "Что желаете #имя#? "
# в противном случае: "#имя#, вы лжете - в наше время столько не живут..."

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
