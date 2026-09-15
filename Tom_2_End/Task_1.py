"""Задание 1 — str / bytes / encode / decode
Создай:
text = "Привет, Python"
Сделай:
encoded = ...
decoded = ...
Требования:
- encoded должен быть bytes;
- кодировка UTF-8;
- decoded снова должен стать обычным str.
Выведи:
print(type(text))
print(type(encoded))
print(type(decoded))

print(text)
print(encoded)
print(decoded)
Потом отдельно:
print(len(text))
print(len(encoded))
"""
text = "Привет, Python"
encoded = text.encode("utf-8")
decoded = encoded.decode("utf-8")
print(type(text))
print(type(encoded))
print(type(decoded))
print(text)
print(encoded)
print(decoded)
print(len(text))
print(len(encoded))