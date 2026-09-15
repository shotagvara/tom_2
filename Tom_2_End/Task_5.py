"""Задание 5 — __getattr__
Создай:
class Config:
Внутри:
self.data = {
    "host": "localhost",
    "port": 5432
}
Сделай:
def __getattr__(self, name):
    ...
так, чтобы:
config.host
config.port
брали значения из self.data.
Но если ключа нет:
config.username
должен возникать нормальный:
AttributeError
Не возвращай просто None.
"""
class Config:
    def __init__(self):
       self.data = {
            "host": "localhost",
            "port": 5432
        }

    def __getattr__(self, name):
        try:
            return self.data[name]
        except KeyError:
            raise AttributeError(f"'Config' object has no attribute '{name}'")

config = Config()
print(config.host)
print(config.por)