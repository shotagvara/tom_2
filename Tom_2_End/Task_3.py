"""Задание 3 — text file vs binary file
Создай файл:
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Привет")
Потом прочитай его два раза:
with open("hello.txt", "r", encoding="utf-8") as f:
    ...
и:
with open("hello.txt", "rb") as f:
    ...
Проверь:
type(...)
В первом случае должен быть str, во втором bytes."""
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Привет")

with open("hello.txt", "r", encoding="utf-8") as f:
    a=(f.read())
    print(a)
    print(type(a))


print("rb:")
with open("hello.txt", "rb") as f:
    a=(f.read())
    print(a)
    print(type(a))