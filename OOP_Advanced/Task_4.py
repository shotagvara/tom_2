"""
Задание 4 — Name mangling + inheritance
Создай:
class Parent:
В __init__:
self.__value = 10
Потом:
class Child(Parent):
и в его __init__:
super().__init__()
self.__value = 20
Создай:
obj = Child()
и выведи:
obj.__dict__
Твоя задача — объяснить, почему внутри одновременно существуют два разных __value.
Это упражнение специально на причину, зачем вообще существует name mangling."""
class Parent:
    def __init__(self):
        self.__value = 10

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__value = 20

obj = Child()

print(obj.__dict__)
#{'_Parent__value': 10, '_Child__value': 20}

#__value в Parent и __value в Child после name mangling превращаются в разные атрибуты: 
# _Parent__value и _Child__value. Поэтому дочерний класс не перезаписывает родительский __value.

#И вот это как раз главная причина, зачем name mangling полезен при inheritance: 
# чтобы subclass случайно не затёр внутренний атрибут parent-класса с тем же именем.