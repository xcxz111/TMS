# Создать родительский класс auto у которого есть атрибуты: brand, age, color, mark и weight.
# А также методы: move, birthday и stop.
# Методы move и stop выводят сообщение на экран "move" и "stop", а birthday увеличивает атрибут age на 1.
# Атрибуты brand, age и mark являются обязательными при объявлении объекта

class Auto:
    def __init__(self, b, a, c=None, m=None, w=None):
        self.brand = b
        self.age = a
        self.color = c
        self.mark = m
        self.weight = w

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1

