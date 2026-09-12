"""Задание 6 — propagation
Сделай:
def level3():
    return 10 / 0

def level2():
    return level3()

def level1():
    return level2()
Ни в одной из функций ошибку не лови.
Лови её только снаружи:
try:
    level1()
except ZeroDivisionError:
    print("Caught outside")
В комментарии объясни:
Почему exception, возникший в level3, удалось поймать снаружи level1?
"""
def level3():
    return 10 / 0

def level2():
    return level3()

def level1():
    return level2()

try:
    level1()
except ZeroDivisionError:
    print("Caught outside")


# ZeroDivisionError occurred in level3.
# Since level3, level2 and level1 did not catch it,
# the exception propagated up the call stack
# until it was caught by the outer try/except.