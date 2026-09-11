"""Задание 16 — cooperative super()
Это самое сложное в блоке.
Создай:
class A:
    def action(self):
        print("A")
Потом B(A) и C(A), где каждый делает:
print("B")
super().action()
или соответственно "C".
Потом:
class D(B, C):
    def action(self):
        print("D")
        super().action()
Вызови:
D().action()
Перед запуском сам предскажи порядок вывода.
Потом:
print(D.__mro__)
и объясни связь.
Это упражнение должно окончательно закрепить:
super() = не обязательно «прямой родитель», а следующий элемент MRO."""
class A:
    def action(self):
        print("A")


class B(A):
    def action(self):
        print("B")
        super().action()


class C(A):
    def action(self):
        print("C")
        super().action()

class D(B,C):
    def action(self):
        print("D")
        super().action()


D().action()
print(D.__mro__)
"""D
B
C
A
(<class '__main__.D'>, <class '__main__.B'>, 
<class '__main__.C'>, <class '__main__.A'>, 
<class 'object'>)"""