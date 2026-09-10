"""Задание 7 — зачем в classmethod именно cls
Добавь:
class Admin(User):
    pass
Теперь вызови:
admin = Admin.from_string("Luka,25")
Проверь:
print(type(admin))
print(isinstance(admin, Admin))
И объясни, почему получился Admin, хотя from_string был написан внутри User.
Вот после этого classmethod действительно должен стать понятен."""
from Task_6 import User
class Admin(User):
    pass

admin = Admin.from_string("Luka,25")
print(type(admin))
print(type(admin.__class__.__name__))
print(admin.__class__)
print(admin.__class__.__name__)
print(isinstance(admin, Admin))

"""<class '__main__.Admin'>
<class 'str'>
<class '__main__.Admin'>
Admin
True
"""

"Потому что в методе фром_стринг мы возвращаем не юзер(), а cls()"
"Пожтому нам будет возрващаться инстанс именно того класса, который вызывает функцию"