"""Задание 9 — hierarchy custom exceptions
Создай:
class AppError(Exception):
    pass

class ValidationError(AppError):
    pass

class AuthenticationError(AppError):
    pass
Потом по очереди выбрасывай:
ValidationError(...)
AuthenticationError(...)
Проверь, что их можно ловить:
- отдельно через ValidationError;
- вместе через AppError.
Это нужно, чтобы руками почувствовать exception inheritance.
"""
class AppError(Exception):
    pass

class ValidationError(AppError):
    pass

class AuthenticationError(AppError):
    pass

try:
    raise ValidationError("Valid error")
except ValidationError as e: 
    print(e)

try:
    raise AuthenticationError("Auth error")
except AuthenticationError as e:
    print(e)

try:
    raise ValidationError("Valid error")
except AppError as e:
     print(e)

try:
    raise AuthenticationError("Auth error")
except AppError as e:
     print(e)

"""Valid error
Auth error
Valid error
Auth error"""