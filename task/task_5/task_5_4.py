# Написать программу, которая ищет числа, делящиеся на 19 или 13 в списке чисел, используя lambda функцию.
# Пример:
# На вход дается список: [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# На выход числа из приведенного выше списка, кратные 19 или 30:
# [19, 65, 57, 39, 152, 190]
# P.S. Для решения может понадобиться использование функции filter

spisok = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
res = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), spisok))
print(res)