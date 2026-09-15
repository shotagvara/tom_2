"""Managed attributes
Задание 4 — property ещё раз, но чуть сложнее
Создай:
Внутри храни:
self._celsius
Сделай:
@property
def celsius(self):
    ...
и setter:
@celsius.setter
def celsius(self, value):
    ...
Правило:
температура не может быть ниже -273.15 °C
Если ниже:
raise ValueError(...)
Добавь read-only property:
@property
def fahrenheit(self):
    ...
Формула:
F = C * 9 / 5 + 32
Но setter для fahrenheit не делай.
Проверь:
t = Temperature(20)

print(t.celsius)
print(t.fahrenheit)

t.celsius = 30
print(t.fahrenheit)
И попробуй:
t.fahrenheit = 100"""
class Temperature:
    def __init__(self, value):
        self.celsius=(value)

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value<-273.15:
            raise ValueError("Слишком низкая температура")
        self._celsius=value

    @property
    def farenheit(self):
        return  self._celsius * 9 / 5 + 32

t = Temperature(-190)

print(t.celsius)
print(t.farenheit)

t.celsius = 30
print(t.farenheit)

t.farenheit = 100
"""AttributeError: property 'farenheit' of 'Temperature' object has no setter"""