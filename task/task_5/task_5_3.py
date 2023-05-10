# Написать программу, которая проверяет, является ли данная строка числом или нет, используя lambda функцию.

symbol = input('введите что нибудь: ')
var = lambda symbol: 'число' if symbol.isdigit() else 'не число'
print(var(symbol))