# 1. Написать калькулятор
# 2. Обернуть его в Tre/except
# 3. Сделать свое исключение и подключить к try/except

class CalculatorError(Exception):
    """Общий класс для ошибок, возникающих в калькуляторе."""
    pass


class ZeroDivisionError(CalculatorError):
    """Ошибка, возникающая при попытке деления на ноль."""
    pass


def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        operation = input("Введите операцию (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль запрещено!")
            result = num1 / num2
        else:
            raise CalculatorError("Неверная операция!")

        print(f"Результат: {result}")

    except ValueError:
        print("Ошибка: неверный формат числа!")
    except CalculatorError as e:
        print(f"Ошибка калькулятора: {e}")
    except ZeroDivisionError as e:
        print(f"Ошибка деления на ноль: {e}")


if __name__ == "__main__":
    calculator()
