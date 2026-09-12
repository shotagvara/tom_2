"""Задание 1 — базовый try / except / else / finally
Напиши функцию:
def divide(a, b):
    ...
Внутри:
- попробуй выполнить a / b;
- если b == 0 и возникает ZeroDivisionError, выведи "Cannot divide by zero";
- если ошибки нет, в else выведи результат;
- в finally всегда выводи "Finished".
Проверь:
divide(10, 2)
divide(10, 0)"""

def divide(a, b):
    try:
        a/b
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else: 
        print(a/b)
    finally:
        print("Finished")

divide(10,2)
divide(10,0)

"""5.0
Finished
Cannot divide by zero
Finished"""