"""Задание 15 — multiple inheritance и MRO
Создай:
class A:
    def work(self):
        return "A"


class B(A):
    def work(self):
        return "B"


class C(A):
    def work(self):
        return "C"


class D(B, C):
    pass
Проверь:
print(D().work())
print(D.__mro__)
Потом поменяй:
class D(C, B):
и снова проверь.
Напиши своими словами:
Почему результат поменялся?"""
class A:
    def work(self):
        return "A"


class B(A):
    def work(self):
        return "B"


class C(A):
    def work(self):
        return "C"


class D(C, B):
    pass

print(D().work())
print(D.__mro__)

"Сначала было В и потом С, но потом стало С В поменялась иерархия наследовнаия"