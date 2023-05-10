
def dm_sm(value: int) -> float:
    res = value * 2.54
    return res


def sm_dm(value: int) -> float:
    res = value * 0.394
    return res


def mil_km(value: int) -> float:
    res = value * 1.61
    return res


def km_mil(value: int) -> float:
    res = value * 0.62
    return res


def ft_kg(value: int) -> float:
    res = value * 0.45
    return res


def kg_ft(value: int) -> float:
    res = value * 2.2
    return res


def yn_gr(value: int) -> float:
    res = value * 28.35
    return res


def gr_yn(value: int) -> float:
    res = value * 0.035
    return res


def gl_lt(value: int) -> float:
    res = value * 4.55
    return res


def lt_gl(value: int) -> float:
    res = value * 0.22
    return res


def pin_lit(value: int) -> float:
    res = value * 0.57
    return res


def lit_pin(value: int) -> float:
    res = value * 1.76
    return res


mapping = {
    1: dm_sm,
    2: sm_dm,
    3: mil_km,
    4: km_mil,
    5: ft_kg,
    6: kg_ft,
    7: yn_gr,
    8: gr_yn,
    9: gl_lt,
    10: lt_gl,
    11: pin_lit,
    12: lit_pin
}

while True:
    menu = int(input(
            'что бы конвертировать введите порядковый номер' + '\n' + '1. Дюймы в сантиметры' + '\n' + '2. Мили в километры' + '\n' + '3. Мили в километры' + '\n' + '4. Километры в мили' + '\n' + '5. Фунты в килограммы' + '\n' + '6. Килограммы в фунты' + '\n' + '7. Унции в граммы' + '\n' + '8. Граммы в унции' + '\n' + '9. Галлон в литры' + '\n' + '10. Литры в галлоны' + '\n' + '11. Пинты в литры' + '\n' + '12. Литры в пинты' + '\n' + 'сделайте ваш выбор: '))
    if 1 <= menu <= 12:
        value = int(input('введите количество: '))
        foo = mapping[menu](value)
        print(foo)
    elif menu == 0:
        break
    else:
        print('вы ввели что то не корректное')





