#  Написать генератор, который будет принимать на вход имя файла и
# генерировать построчно(т.е yield каждой строки).

def read_file_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


for line in read_file_lines('file'):
    print(line)
