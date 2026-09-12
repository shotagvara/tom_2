"""Задание 10 — assert
Создай:
def get_first(items):
    assert len(items) > 0, "items must not be empty"
    return items[0]
Проверь:
get_first([1, 2, 3])
get_first([])
И в комментарии напиши:
Почему такой assert может быть допустим как внутренняя проверка предположения, но плох как validation пользовательского ввода?
"""

def get_first(items):
    assert len(items)>0, "item must not be empty"
    return items[0]

print(get_first([1,2,3]))
print(get_first([]))
"""
1
Traceback (most recent call last):
    print(get_first([]))
          ^^^^^^^^^^^^^
    assert len(items)>0, "item must not be empty"
           ^^^^^^^^^^^^
AssertionError: item must not be empty"""

"""assert
→ проверка предположений программиста

if ...: raise ...
→ нормальная validation данных"""