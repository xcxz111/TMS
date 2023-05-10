# 1. Создать свой класс данных
# 2. Добавить в класс статикметод
# 3. Добавить в класс классметод
# 4. Создать метакласс

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @staticmethod
    def get_oldest_person(people):
        return max(people, key=lambda person: person.age)

    @classmethod
    def from_string(cls, string):
        first_name, last_name, age = string.split(',')
        return cls(first_name.strip(), last_name.strip(), int(age.strip()))


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args)
