# создать две переменные с одинаковыми данными и с разными индефикаторами

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a))
print(id(b))

from copy import deepcopy

c = [1, 1, 1]
d = deepcopy(c)
print(id(c))
print(id(d))