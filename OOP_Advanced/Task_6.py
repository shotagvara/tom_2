"""Задание 6 — @classmethod
Создай:
class User:
Обычный constructor:
def __init__(self, name, age):
Потом alternative constructor:
@classmethod
def from_string(cls, text):
    ...
Строка:
"Shota,21"
должна превратиться в:
User("Shota", 21)
То есть:
user = User.from_string("Shota,21")
должен создать нормальный объект.
Обязательно используй внутри:
cls(...)
а не:
User(...)"""
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, text):
        a, b = text.strip().split(",")
        return cls(a, int(b))

    def __str__(self):
        return(f"{self.name}, {self.age}")



if __name__=="__main__":
    user1 = User.from_string("Shota,21")
    print(user1.__str__())

    a, b ="Shota,21".strip().split(",")
    print(a, b)