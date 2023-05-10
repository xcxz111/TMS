#  Написать свой итератор(реализовать у него и метод __next__ и __iter__), чтобы
# при обходе циклом он отдавал только элементы на четных индексах,
# возведенные в квадрат.

class Iterator:
    def __init__(self, l_):
        self.l_ = l_
        self.cursor = 0

    def __next__(self):
        if self.cursor >= len(self.l_):
            raise StopIteration

        value = self.l_[self.cursor]**2
        self.cursor += 2
        return value


class A:
    def __init__(self, l_):
        self.l_ = l_

    def __iter__(self):
        return Iterator(self.l_)


a = A([1, 2, 3, 4, 5, 6, 7, 8, 9])


for i in a:
    print(i)