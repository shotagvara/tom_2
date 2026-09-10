"""
Задание 10 — свой __next__
Теперь отдельно, потому что это важная тема.
Создай:
class Countdown:
Например:
countdown = Countdown(3)
Должно работать:
next(countdown)  # 3
next(countdown)  # 2
next(countdown)  # 1
а потом:
next(countdown)
должно вызвать:
StopIteration
Нужно самостоятельно написать:
__iter__
__next__
Условие:
iter(countdown) is countdown
должно быть True.
И в комментарии ответь:
Почему Countdown является iterator, а не просто iterable?"""
class Countdown:
    def __init__(self, start):
        self.counter = start


    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= 0:
            raise StopIteration
        self.counter-=1
        return self.counter+1

countdown = Countdown(3)
print(next(countdown))
print(next(countdown))
print(next(countdown))

print(iter(countdown) is countdown)
print(next(countdown))

"""3
2
1
True
Traceback (most recent call last):
    print(next(countdown))
          ^^^^^^^^^^^^^^^
    raise StopIteration
StopIteration
"""