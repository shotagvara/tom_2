"""Задание 13 — composition
Создай:
class Engine:
с методом:
start()
Потом:
class Car:
Car должен получать Engine в __init__:
self.engine = engine
И:
car.start()
должен внутри использовать:
self.engine.start()
После этого в комментарии:
Почему здесь Car HAS-A Engine,
а наследование Car(Engine) было бы плохой моделью?"""

class Engine:
    def start(self):
        return("Engine started")

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

engine = Engine()
car = Car(engine)
print(car.start())

"""Engine — составная часть Car, поэтому здесь подходит composition. 
Inheritance был бы неправильным, потому что Car не является типом Engine."""