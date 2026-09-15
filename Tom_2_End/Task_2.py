"""Задание 2 — bytes vs bytearray
Создай:
data = b"ABC"
Проверь:
print(data[0])
print(data[0:1])
Потом попробуй:
data[0] = 70
Посмотри ошибку.
После этого:
mutable_data = bytearray(b"ABC")
измени первый элемент на 70.
Выведи результат.

"""
data = b"ABC"

print(data[0])
print(data[0:1])
"""
data[0]=70
TypeError: 'bytes' object does not support item assignment"""
mutable_data= bytearray(b"ABC")
mutable_data[0]=70
print(mutable_data)