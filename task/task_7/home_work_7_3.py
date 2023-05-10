import time


class Auto:
    def __init__(self, brand, age, color, mark, weight):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


class Truck(Auto):
    def __init__(self, brand, age, color, mark, weight, max_load):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load

    def move(self):
        super().move()
        print("attention")

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, age, color, mark, weight, max_speed):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max_speed is {self.max_speed}")


truck1 = Truck("MAN", 2, "white", "X9", 5000, 1500)
truck2 = Truck("Scania", 3, "red", "R124", 5500, 2000)
car1 = Car("BMW", 1, "black", "X5", 2000, 240)
car2 = Car("Audi", 4, "silver", "Q7", 2300, 260)

truck1.move()
truck1.load()
print(truck1.max_load)
truck1.stop()


car1.move()
print(car1.max_speed)
car1.birthday()
car1.move()
car1.stop()
