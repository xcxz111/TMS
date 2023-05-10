# Ввести с клавиатуры 4 строки и сохранить их в 4 разные переменные.
# Создать файл и записать в него первые 2 строки и закрыть файл.
# Затем открыть файл на редактирование и дописать оставшиеся 2 строки.В итоговом файле должны быть 4 строки,
# каждая из которых должна начинаться с новой строки.

one = input('введите первую строку: ')
two = input('введите вторую строку: ')
three = input('введите третью строку: ')
four = input('введите четвертую строку: ')

f = open("test.txt", "w")
f.write(one)
f.write('\n')
f.write(two)
f.close()
f = open("test.txt", "a")
f.write('\n')
f.write(three)
f.write('\n')
f.write(four)
f.close()

# with open("C:/Users/Brodi/PycharmProjects/tech_me_skills/task/task_6/test.txt", "w") as f:
#     f.write(one)
#     f.write('\n')
#     f.write(two)
#     f.write('\n')
#     f.write(three)
#     f.write('\n')
#     f.write(four)
