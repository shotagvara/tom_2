"""Задание 12 — inheritance + polymorphism + super()
Создай:
class Animal:
с:
speak()
Потом:
Dog(Animal)
Cat(Animal)
Каждый переопределяет:
speak()
Создай:
animals = [Dog(...), Cat(...), Dog(...)]
и:
for animal in animals:
    print(animal.speak())
Здесь задача — показать polymorphism."""
class Animal:
    def speak(self):
        return("SOUND")

class Dog(Animal):
    def speak(self):
        return("GAV GAV")

class Cat(Animal):
    def speak(self):
        return("MEOU")

dog = Dog()
cat = Cat()
animalo = Animal()

animals  = [animalo, cat, dog]
for animal in animals:
    print(animal.speak())

"""SOUND
MEOU
GAV GAV"""