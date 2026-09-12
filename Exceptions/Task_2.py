"""Задание 2 — несколько типов ошибок
Напиши функцию:
def parse_and_divide(text, divisor):
    ...
Она должна:
1. преобразовать text в int;
2. разделить число на divisor.
Отдельно обработай:
- ValueError — если text нельзя преобразовать в число;
- ZeroDivisionError — если делишь на 0.
Например:
parse_and_divide("100", 5)
parse_and_divide("hello", 5)
parse_and_divide("100", 0)"""
def parse_and_divide(text, divisor):
    try:
        result = int(text)/divisor
    except ValueError:
        print("text нельзя преобразовать в число")
    except ZeroDivisionError:
        print("Cannot divide by 0")
    else:
        print(result)
    finally:
        print("FINITO")

parse_and_divide("100", 5)
parse_and_divide("hi", 5)
parse_and_divide(100, 0)
"""20.0
FINITO
text нельзя преобразовать в число
FINITO
Cannot divide by 0
FINITO"""