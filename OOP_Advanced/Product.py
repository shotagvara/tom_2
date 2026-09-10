class Product:
    def __init__(self, name, price):
        self.name=name
        self.price=price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price must be >= 0")
        self._price=price

    @property
    def price_wtih_tax(self):
        return self._price*1,19

    