"""Создай Book с title, author, price. 
Создай 3 объекта, выведи __dict__, __class__ и проверь через is, что объекты разные."""

class Book:
    category = "Books"
    def __init__(self, title: str, author: str, price: float): 
        self.title=title
        self.author=author
        self.price=price

book1= Book("Book nr 1", "Shota", 20.0)
book2= Book("Book nr 2", "Luka", 25.0)
book3= Book("Book nr 3", "ShotaLuka", 29.0)

print(book1.__dict__)
print(book2.__dict__)
print(book3.__dict__)
print(book1.__class__)
print(book2.__class__)
print(book3.__class__)
print(book1 is book2)
print(book1 is Book)
print(isinstance(book1, Book))
print(book1 is book2)
print(book1 is book3)
print(book2 is book3)

"""1. Добавь class attribute:
category = "Books"
У одного объекта присвой свою category. 
Объясни в комментарии, почему остальные объекты не изменились."""

book1.category="New book category"
print(book2.category)
print(book1.__dict__)
print(book2.__dict__)
print(book3.__dict__)

# book1 gets its own instance attribute `category`,
# which shadows the class attribute Book.category.
# book2 and book3 still use Book.category.