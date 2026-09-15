"""Задание 7 — первый function decorator
Создай:
def logger(func):
    ...
Он должен перед вызовом функции писать:
Calling function
и после:
Function finished
Применяй к:
@logger
def greet(name):
    return f"Hello, {name}"
Проверь:
print(greet("Shota"))
Важно:
- используй *args, **kwargs;
- верни результат исходной функции.
"""
def logger(func):
    def wrapper(*args, **kwargs):
        print("Caliing function")

        result = (func(*args, **kwargs))

        print("Function finished")
        return result

    return wrapper

@logger 
def greet(name):
    return f"Hello, {name}"

print(greet("Shota"))