"""
Задание 5 — @staticmethod
Создай:
class PasswordValidator:
Внутри:
@staticmethod
def is_valid(password):
    ...
Правила можешь сделать простыми:
- минимум 8 символов;
- должна быть хотя бы одна цифра.
Использование:
print(PasswordValidator.is_valid("hello"))
print(PasswordValidator.is_valid("hello123"))
После этого создай instance:
validator = PasswordValidator()
и попробуй:
validator.is_valid("python123")
В комментарии ответь:
Что Python автоматически передал staticmethod первым аргументом?
Ожидаемый ответ потом обсудим."""
class PasswordValidator:
    @staticmethod
    def has_digit(passwort):
        for char in passwort:
            if char.isdigit():
                return True
        return False
    
    @staticmethod
    def is_valid(passwort: str):
        return (len(passwort)>=8 and PasswordValidator.has_digit(passwort))

 

print(PasswordValidator.is_valid("hello123"))
print(PasswordValidator.is_valid("hello"))
validator = PasswordValidator()
print(validator.is_valid("python123"))

"""
При:
a.normal()
Python автоматически передаёт a как self.
У classmethod:
@classmethod
def method(cls):
    ...
Python автоматически передаёт класс как cls.
А у:
@staticmethod
def is_valid(password):
    ...
никакого автоматического аргумента нет."""
