"""
Задание 2 — отдельный getter с вычислением
Расширь Product.
Добавь:
@property
def price_with_tax(self):
    ...
Он должен возвращать цену с НДС, например +19%.
Но setter для price_with_tax не делай.
То есть:
print(p.price_with_tax)
работает.
А:
p.price_with_tax = 500
не должно нормально работать.
Здесь ты увидишь разницу между:
- read/write property;
- read-only property."""

from Product import Product

p = Product("Laptop", 1000)

print(p.price_wtih_tax)
p.price_wtih_tax = 500

"""
(1000, 19)
Traceback (most recent call last):
  File "c:\Users\Amstel\Desktop\Innowise Praktikum\Tom2\OOP_Advanced\Task_2.py", line 25, in <module>
    p.price_wtih_tax = 500
    ^^^^^^^^^^^^^^^^
AttributeError: property 'price_wtih_tax' of 'Product' object has no setter
PS C:\Users\Amstel\Desktop\Innowise Praktikum\Tom2> 
"""