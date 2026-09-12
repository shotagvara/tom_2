"""Задание 3 — raise
Создай функцию:
def set_age(age):
    ...
Если:
age < 0
то сам выбрасывай:
ValueError("Age cannot be negative")
Иначе возвращай age.
Проверь:
print(set_age(21))
print(set_age(-5))"""
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


print(set_age(20))
print(set_age(-5))
"""20
Age cannot be negative
"""