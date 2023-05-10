# Написать свой класс MyOpen, объекты которого должны поддерживать
# протокол контекстного менеджера. Он должен работать аналогично with
# open(‘file.txt’, ‘w+’) as f. Т.е вы можете применять его следующим образом:
# with MyOpen(file.txt’, ‘w+’) as f

class MyOpen:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
