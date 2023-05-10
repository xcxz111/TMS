# Написать декоратор, который будет выводить время выполнения функции,
# а также аргументы, с которыми она была вызвана.

# 1. Написать декоратор, он должен будет выводить время выполнения функции, а также аргументы,
#    с которыми она была вызвана.

import time


def time_arg(x):
    def wrapper(*args, **kwargs):
        startTime = time.perf_counter()  # время начала замера
        res = x(*args, **kwargs)
        print(res)
        endTime = time.perf_counter()  # время конца замера
        totalTime = endTime - startTime  # вычисляем затраченное время
        print(f'Время, затраченное на выполнение данного кода = {totalTime} сек.')
        print('Аргумент с которым была вызвана функция:', *args, **kwargs)

        return res

    return wrapper


@time_arg
def fibo(n):
    fib1 = 1
    fib2 = 1

    i = 0
    while i < n - 2:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2


fibo(10000)
