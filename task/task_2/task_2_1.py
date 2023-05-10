# создать 3 переменные с одинаковыми данными и с одинаковыми индефикаторами
a = 2
b = a
c = a
print(id(a))
print(id(b))
print(id(c))

aa, bb, cc = 1, 1, 1
print(id(aa), id(bb), id(cc))
