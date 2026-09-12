"""Задание 5 — custom exception со state
Создай:
class NotEnoughMoneyError(Exception):
    ...
Он должен хранить:
balance
required
И сообщение вроде:
Required 500, but balance is 100
Потом создай:
class Wallet:
с:
- balance
- spend(amount)
Если денег недостаточно — выбрасывай NotEnoughMoneyError.
Потом:
try:
    wallet.spend(...)
except NotEnoughMoneyError as e:
    print(e)
    print(e.balance)
    print(e.required)
"""
class NotEnoughMoneyError(Exception):
    def __init__(self, balance, required):
        self.balance = balance
        self.required = required
        super().__init__(
            f"\nRequired {required}, \nbut balance is {balance}"
        )



class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def spend(self, amount):
        if (amount>self.balance):
            raise NotEnoughMoneyError(self.balance, amount)
        self.balance = self.balance - amount

wallet = Wallet(100)
wallet.spend(500)
print(wallet.balance)
            