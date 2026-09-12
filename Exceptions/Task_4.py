"""Задание 4 — custom exception
Создай свой exception:
class InvalidPasswordError(Exception):
    pass
Потом функцию:
def validate_password(password):
    ...
Если пароль короче 8 символов:
raise InvalidPasswordError(...)
Потом поймай именно:
except InvalidPasswordError as e:
и выведи сообщение."""

class InvalidPasswordError(Exception):
    pass

def validate_password(password):
    if len(password)<8:
        raise InvalidPasswordError("Password must contain at least 8 characters")

try:
    validate_password("haha")
except InvalidPasswordError as e:
    print(e)

    
"""Password must contain at least 8 characters"""
