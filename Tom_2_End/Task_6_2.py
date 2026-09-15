class NonEptyString:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if isinstance(value, str) == False:
            raise TypeError("Value must be a string")        
        else:
            if (value == ""):
                raise ValueError(f"String cannot be empty")
            
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    
class User:
    name = NonEptyString()
    city = NonEptyString()

    def __init__(self, name, city):
        self.name = name
        self.city = city

u1 = User("Shota", "Berlin")
u2 = User("Luka", "Hamburg")

print(u1.name)
print(u1.city)

print(u2.name)
print(u2.city)