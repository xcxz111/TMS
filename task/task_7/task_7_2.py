# Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
# Методы : увеличение скорости (скорость +5), уменьшение скорости (скорость -5), стоп(сброс скорости на 0),
# отображение скорости, разворот (изменение знака скорости). Все атрибуты приватные


class Car:
    def __init__(self, m, mod, y, s=0):
        self.__brand = m
        self.__model = mod
        self.__year = y
        self.__speed = s

    def plus_speed(self):
        self.__speed += 5

    def min_speed(self):
        self.__speed -= 5

    def stop_speed(self):
        self.__speed = 0

    def pr_speed(self):
        return self.__speed

    def reverse(self):
        self.__speed = -self.__speed
        print(self.__speed)


car1 = Car('audi', 'a4', 2000, 60)




