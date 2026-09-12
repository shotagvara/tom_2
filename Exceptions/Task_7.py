"""Задание 7 — bare raise
Напиши:
def parse_number(text):
    try:
        return int(text)
    except ValueError:
        print("Logging error...")
        raise
Потом снаружи:
try:
    parse_number("abc")
except ValueError:
    print("Caught again")
Объясни, почему один и тот же ValueError сначала попал во внутренний except, а потом ещё и во внешний.
"""
def parse_number(text):
    try:
        return int(text)
    except ValueError:
        print("Logging error...")
        raise

try:
    parse_number("abc")
except ValueError:
    print("Caught again")

#Потому что мы снова его зарэйзили после того как словили
