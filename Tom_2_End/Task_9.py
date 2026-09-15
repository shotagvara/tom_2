"""Задание 9 — decorator с аргументами + wraps
Создай:
@repeat(3)
def say_hi(name):
    print(f"Hi, {name}")
Нужно реализовать:
def repeat(times):
    ...
с тремя уровнями:
- repeat
- decorator
- wrapper
И используй:
from functools import wraps
Потом проверь:
print(say_hi.__name__)
Он должен остаться:
say_hi
а не wrapper.
Бонус — class decorator
Если захочешь, после этих девяти сделаем ещё два бонусных:
@add_repr
class User:
    ...
и маленький пример с:
type(...)
или custom metaclass.
Но это уже после основной части."""

from functools import wraps

def repeat(times):
    pass



@repeat(3)
def say_hi(name):
    print(f"Hi, {name}")