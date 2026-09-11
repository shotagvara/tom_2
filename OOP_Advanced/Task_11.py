"""Задание 11 — reusable iterable
Теперь сделай другой класс:
class NumberRange:
Чтобы:
numbers = NumberRange(3)

print(list(numbers))
print(list(numbers))
оба раза выводили:
[0, 1, 2]
Не храни один исчерпываемый iterator внутри самого объекта.
Можно реализовать:
def __iter__(self):
    return iter(range(...))
или через yield.
Потом сравни с Countdown.
Это очень важное упражнение:
iterable ≠ iterator"""

class NumberRange:
    def __init__(self, number):
        self.number = number

    def __iter__(self):
        for x in range(self.number):
            yield x

  

numbers = NumberRange(4)

print(list(numbers))
print(list(numbers))

"""Countdown
- сам хранит состояние
- имеет __next__
- __iter__ возвращает self
- single-pass

NumberRange
- сам не хранит позицию итерации
- __next__ не нужен
- __iter__ создаёт новый iterator
- reusable"""