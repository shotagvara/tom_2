"""Задание 11 — with и cleanup
Открой файл:
with open("example.txt", "w") as f:
    f.write("Hello")
После блока проверь:
print(f.closed)
Должно быть:
True
И объясни, почему with удобнее ручного:
open(...)
...
close()
Начни с 1–4. Кидай код, я проверю. Потом пойдём дальше по propagation, raise from, hierarchy и with."""
with open("example.txt", "w") as f:
    f.write("Hello")

print(f.closed)


"True"

"""with
→ сам гарантирует cleanup
→ файл закроется даже если внутри блока возникнет exception


При ручном подходе:
можно забыть close() или не дойти до него из-за ошибки."""

