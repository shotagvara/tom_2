"""
Создай класс:
class Product:
    ...
Поля:
name
_price
Конструктор принимает:
Product(name, price)
Но price должен управляться через property.
Нужно реализовать:
@property
def price(self):
    ...
и:
@price.setter
def price(self, value):
    ...
Правила:
- цена должна быть >= 0;
- если передали отрицательное значение — ValueError;
- при чтении product.price возвращается _price.
Проверь:
p = Product("Laptop", 1200)
print(p.price)
p.price = 1500
print(p.price)
p.price = -100
Последняя строка должна вызвать ошибку.
Важно: в __init__ попробуй использовать именно:
self.price = price
а не напрямую:
self._price = price
Подумай, почему первый вариант полезнее."""

from Product import Product

p = Product("Laptop", 1200)
print(p.price)
p.price = 1500
print(p.price)
p.price = -100
            
"""
Потому что 
self.price = price в __init__ проходит через setter, а 
self._price = price — обходит его.
"""