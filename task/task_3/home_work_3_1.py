# Ввести предложение состоящее из двух слов. Поменять местами слова,
# добавить восклицательный знак в начало и в конец,
# слова разделить 3 символами (пробел, восклицательный знак и еще пробел),
# вывести итоговое предложение на экран.
# Задание необходимо выполнить 3-мя разными способами форматирования.

[a_1, b_1] = input('введите два слова: ').split()
a_1, b_1 = b_1, a_1
print('!' + a_1 + ' ! ' + b_1 + '!')

[a_2, b_2] = input('введите два слова: ').split()
print(f'!{b_2} ! {a_2}!')

a_3 = input('введите два слова: ').split()
print('!' + ' ! '.join([str(i) for i in a_3[::-1]]) + '!')
