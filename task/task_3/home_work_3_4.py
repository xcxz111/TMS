# Ввести с клавиатуры целое число n.
# Получить сумму кубов всех целых чисел от 1 до n(включая n)
# Реализовать в 2-х вариантах: используя цикл while и цикл for

# n_1 = int(input('Введите число n: '))
# i = 1
# summa = 0
# while i <= n_1:
#     x = i**3
#     i += 1
#     summa += x
# print(summa)


n_2 = int(input('Введите число n: '))
summa = 0
for i in range(n_2+1):
    x = i ** 3
    summa += x
print(summa)

