"""4. Создай:
class Employee
с name, salary и describe(). Затем:
class Developer(Employee)
с дополнительным language и переопредели describe().
5. Переделай Developer.__init__, чтобы общие данные задавались через:
super().__init__(...)
Затем добавь:
class SeniorDeveloper(Developer)
с level.
6. Создай список:
employees = [
    Employee(...),
    Developer(...),
    SeniorDeveloper(...)
]
и одним циклом вызывай:
employee.describe()
"""

class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

    def describe(self):
        return f"Employee\nname: {self.name}\nsalary: {self.salary}\n"

    def __str__(self):
        return (
            f"{self.__class__.__name__}\n"
            f"name: {self.name}\n"
            f"salary: {self.salary}"
        )

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language=language

    def describe(self):
        return super().describe()+f"language: {self.language}\n"

    def __str__(self):
        return super().__str__() + f"\nlanguage: {self.language}"

    
class SeniorDeveloper(Developer):
    def __init__(self, name, salary, language, level):
        super().__init__(name, salary, language)
        self.level=level

    def describe(self):
        return super().describe()+f"level: {self.level}"

    def __str__(self):
            return super().__str__() + f"\nlevel: {self.level}"
    


empl1= Employee("Shota", 10000)
empl2_dev= Developer("Luka", 15000, "C++")
empl3_senior_dev= SeniorDeveloper("Vaso", 20000, "Python", "superLevel")

emloyees=[empl1, empl2_dev, empl3_senior_dev]

for employee in emloyees:
    print(employee)


"""Employee
name: Shota
salary: 10000
Developer
name: Luka
salary: 15000
language: C++
SeniorDeveloper
name: Vaso
salary: 20000
language: Python
level: superLevel
"""