"""class BankAccount:
    ...
У него должны быть:
- owner
- balance
Методы:
- deposit(amount) — увеличить баланс
- add_interest(percent) — начислить проценты
- __str__() — красиво вывести владельца и баланс
Потом:
class PremiumAccount(BankAccount):
    ...
Добавь:
- bonus_percent
И переопредели:
add_interest(percent)
так, чтобы:
1. сначала через super() сработала обычная логика BankAccount,
2. потом дополнительно начислился бонус.
Пример логики по смыслу:
balance = 1000
interest = 10%
bonus = 2%

после обычного процента:
1100

потом дополнительный bonus:
ещё +2%
Как именно считать бонус — выбери сам и просто будь последовательным.
После этого:
account = PremiumAccount(...)
сделай:
- deposit(...)
- add_interest(...)
- print(account)
Потом сохрани объект через pickle:
import pickle
и после загрузки проверь:
print(loaded_account)
print(type(loaded_account))
print(isinstance(loaded_account, PremiumAccount))
И ещё вызови у загруженного объекта один метод, чтобы убедиться, 
что он не просто данные сохранил, а реально восстановился как объект класса.
Как закончишь — кидай код. Я проверю, и после этого идём к следующему блоку Лутца.
"""
import pickle

class BankAccount:
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance

    def deposit(self, ammount):
        self.balance =self.balance + ammount

    def add_interest(self, percent):
        self.balance*=(1+percent/100)

    def __str__(self):
        return (f"BankAccount\n"
                f"Owner: {self.owner}"
                f"Balance: {self.balance}")

class PremiumAccount(BankAccount):
    def __init__(self, owner, balance, bonus_percent):
        super().__init__(owner, balance)
        self.bonus_percent=bonus_percent

    def add_interest(self, percent):
        super().add_interest(percent)
        self.balance *= (1 + self.bonus_percent / 100)
        

account = PremiumAccount("Shota", 0, 20)

account.deposit(1000)
account.add_interest(20)
print(account)

with open("account.pkl", "wb") as f:
    pickle.dump(account, f)

with open("account.pkl", "rb") as f:
    reloaded= pickle.load(f)

print("Reoload: ")
print(reloaded)

print(type(reloaded))
print(isinstance(reloaded, PremiumAccount))

reloaded.deposit(100)
print(reloaded)