"""Задание 8 — raise ... from ...
Напиши функцию:
def load_age(text):
    ...
Внутри попробуй:
int(text)
Если возникает ValueError, выброси новую ошибку:
class InvalidAgeFormatError(Exception):
    pass
Пример:
raise InvalidAgeFormatError(
    "Age must be a number"
) from e
Потом вызови:
load_age("hello")
и посмотри traceback.
Твоя задача — объяснить, почему Python показывает две связанные ошибки.
"""
class InvalidAgeFormatError(Exception):
    pass

    
        


def load_age(text):
    try:
        return int(text)
    except ValueError as e:
        raise InvalidAgeFormatError(
            "Age must be a number"
        ) from e

load_age("hello")
