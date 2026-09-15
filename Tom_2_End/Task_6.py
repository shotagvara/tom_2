"""Задание 6 — descriptor
Создай descriptor:
class PositiveNumber:
Он должен не позволять сохранять отрицательные значения.
Используй:
- __set_name__
- __get__
- __set__
Потом:
class Product:
    price = PositiveNumber()
    weight = PositiveNumber()
И проверь:
p = Product()
p.price = 100
p.weight = 2.5

print(p.price)
print(p.weight)

p.price = -10
Это упражнение нужно, чтобы почувствовать, зачем descriptor полезнее, чем писать одинаковый property несколько раз.
Decorators
"""
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value cannot be negative")

        instance.__dict__[self.name] = value

class Product:
     price = PositiveNumber()
     weight = PositiveNumber()


p = Product()
p.price = 100
p.weight = 2.5

print(p.price)
print(p.weight)





    

    