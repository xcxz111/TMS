#  Просмотреть ваше задание, где вы реализовывали класс Car и подумать, где
# стоит добавить выкидывание(raise) исключений(например, когда скорость
# может стать меньше 0). В месте, где вы работаете с этим классом, добавьте
# обработку этих исключений, используя конструкцию try.

class Car:
    def __init__(self, m, mod, y, s=0):
        self.__brand = m
        self.__model = mod
        self.__year = y
        self.speed = s

    def plus_speed(self):
        self.speed += 5

    def min_speed(self):
        self.speed -= 15
        if self.speed < 0:
            raise ValueError("скорость меньше минимальной")
        return self.speed

    def stop_speed(self):
        self.speed = 0

    def pr_speed(self):
        return self.speed

    def reverse(self):
        self.speed = -self.speed
        print(self.speed)


car1 = Car("Toyota", "Camry", 2022, 10)


try:
    print(car1.min_speed())
except ValueError as e:
    print(e)


