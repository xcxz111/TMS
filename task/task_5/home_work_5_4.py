# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
# Подсказка:
# from datetime import datetime
# time = datetime.now()

from datetime import datetime
import time


def decorating_func(own_func):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return own_func

@decorating_func
def addition(num1,num2):
    return num1 + num2

@decorating_func
def multiply(num1,num2):
    return num1 * num2



