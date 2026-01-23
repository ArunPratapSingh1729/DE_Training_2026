from enum import Enum, unique

@unique
class Department(Enum):
    HR = "HR Department"
    DE = "Data Engineering"
    DS = "Data Science"


class Employee:
    def __init__(self, id, name, department: Department):
        self.id = id
        self.name = name
        self.department = department


class HRManager(Employee):
    def __init:
    def __init__(self, id, name):
        super().__init__(id, name, Department.HR)

    def work(self):
        return f"{self.name} is managing recruitment and employee relations."


class PythonDeveloper(Employee):
    def __init__(self, id, name):
        super().__init__(id, name, Department.DE)

    def work(self):
        return f"{self.name} is a python code developer"


class DataScientist(Employee):
    def __init__(self, id, name):
        super().__init__(id, name, Department.DS)

    def work(self):
        return f"{self.name} is a Data Scientist"


e = Employee(1, 'arun', Department.DE)
print(e.id)
print(e.name)
print(e.department)
print(e.department.value)
