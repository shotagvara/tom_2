"""
Задание 8 — __str__ и __repr__
Создай:
class Movie:
Поля:
title
year
Реализуй оба:
__str__
__repr__
Например по смыслу:
print(movie)
должно давать красивый пользовательский вариант.
А:
repr(movie)
более технический:
Movie(title='Interstellar', year=2014)
Проверь:
print(movie)
print(str(movie))
print(repr(movie))
И объясни разницу."""
class Movie:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year})"

    def __repr__(self):
        return (f"{self.__class__.__name__}(title={self.title!r}, year={self.year!r})")

movie = Movie("Interstellar", 2014)
print(movie.__str__())
print(movie.__repr__())
print(repr(movie))
print(str(movie))

"__repr__ для разработчиков, а __str__ для пользователя красивое представление"
        