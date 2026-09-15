"""Задание 8 — decorator со state
Создай:
def count_calls(func):
Он должен считать, сколько раз вызвали decorated function.
Используй closure и:
nonlocal
Например:
@count_calls
def hello():
    print("Hello")
После трёх вызовов ожидай что-то вроде:
Call #1
Call #2
Call #3
"""

def count_calls(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count+=1

        print(f"Call #{count}")  

        return func(*args, **kwargs)

    return wrapper

@count_calls
def hello():
    print("Hello")

hello()
hello()
hello()
hello()

          
    
