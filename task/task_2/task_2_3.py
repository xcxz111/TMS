# поменять их типы так, чтобы у 1-х трёх были разные индефикаторы,
# а у 2х последних были одинаковые индефикаторы
from copy import deepcopy
a = 2
b = a
c = a
d = [1, 1, 1]
e = deepcopy(c)
print(id(a), id(b), id(c), id(d), id(e))  # индефикаторы из заданий 1,2

a = str(a)
b = str(b)
c = str(c)
d = tuple(d)
e = d
print(id(a), id(b), id(c), id(d), id(e))