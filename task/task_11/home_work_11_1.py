# Создать генератор геометрической прогрессии
# Подключить дебаггинг
# Сделать функцию для фильтрации email


def geometric_progression(start, factor):
    current = start
    while True:
        yield current
        current *= factor


gp = geometric_progression(2, 2)
print(next(gp))
print(next(gp))
print(next(gp))