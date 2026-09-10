"""Задание 3 — Name mangling
Создай:
class BankCard:
Поля:
owner
__pin
Методы:
check_pin(pin)
change_pin(old_pin, new_pin)
Например:
card = BankCard("Shota", 1234)

print(card.check_pin(1234))
# True
После этого попробуй:
print(card.__pin)
Посмотри, что произойдёт.
Потом:
print(card.__dict__)
И найди настоящее имя, которое Python создал после name mangling.
После этого попробуй обратиться к нему напрямую через изменённое имя.
В комментарии ответь:
Почему __pin не является настоящей защитой/security?
И ещё добавь:
self._card_number
чтобы самому увидеть отличие:
_name
от:
__name"""
class BankCard:
    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin

    def check_pin(self, pin):
        return self.__pin == pin

    def change_pin(self, old_pin, new_pin):
        if self.__pin == old_pin:
            self.__pin = new_pin
            return True
        return False

card = BankCard("Shota", 1234)

print(card.check_pin(1234))
# True
#print(card.__pin)

"""
Traceback (most recent call last):
    print(card.__pin)
          ^^^^^^^^^^
AttributeError: 'BankCard' object has no attribute '__pin'
"""
print(card.__dict__)
#{'owner': 'Shota', '_BankCard__pin': 1234}

print(card._BankCard__pin)
#1234
