# Создать 2 класса truck и car, которые являются наследниками класса auto.
# Класс truck имеет дополнительный обязательный атрибут max_load.
# Переопределенный метод move, после появления надписи "move" выводит надпись "attention",
# реализацию сделать при помощи оператора super. А так же дополнительный метод load.
# При его вызове происходит пауза 1 сек., затем выдается сообщение "load" снова пауза 1 сек.
# Класс car имеет дополнительный обязательный атрибут max_speed и при вызове метода move,
# после появления надписи "move" должна появиться надпись "max_speed is <max_speed>".
# Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты

import time


class Auto:
    def __init__(self, brand, age, color=None, mark=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1


class Truck(Auto):
    def __init__(self, max_load, brand, age, color=None, mark=None, weight=None):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        super().move()
        print('attention')

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


class Car(Auto):
    def __init__(self, max_speed, brand, age, color=None, mark=None, weight=None):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max_speed is {self.max_speed}')


truck1 = Truck(1500, 'BMW', 2, 'white')
truck2 = Truck(2000, 'Audi', 3, 'Blue')
car1 = Car(240, 'BMW', 1, 'black', 'X5')
car2 = Car(260, 'Audi', 4, 'silver', 'Q7')


print(f'brand: {truck1.brand}')
print(f'age: {truck1.age}')
print(f'color: {truck1.color}')
print(f'mark: {truck1.mark}')
print(f'weight: {truck1.weight}')
print(f'max_load: {truck1.max_load}')
print('----------\n')
truck1.move()
truck1.load()
truck1.birthday()
truck1.stop()

print('----------\n')

print(f'brand: {car1.brand}')
print(f'age: {car1.age}')
print(f'color: {car1.color}')
print(f'mark: {car1.mark}')
print(f'weight: {car1.weight}')
print(f'max_speed: {car1.max_speed}')
print('----------\n')
car1.move()
car1.birthday()
car1.move()
car1.stop()

