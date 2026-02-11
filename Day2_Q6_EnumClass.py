from enum import Enum, unique


@unique
class Department(Enum):
    HR = "HR Department"
    DE = "Data Engineering"
    DS = "Data Science"


class Employee:
    def __init__(self, id, name, department: Department):
        try:
            self.id = int(id)
            self.name = str(name)

            if not isinstance(department, Department):
                raise TypeError("department must be a Department enum")

            self.department = department

        except Exception as e:
            raise ValueError("Invalid Employee initialization") from e


class HRManager(Employee):
    def __init__(self, id, name):
        try:
            super().__init__(id, name, Department.HR)
        except Exception as e:
            raise ValueError("Invalid HRManager initialization") from e

    def work(self):
        return f"{self.name} is managing recruitment and employee relations."


class PythonDeveloper(Employee):
    def __init__(self, id, name):
        try:
            super().__init__(id, name, Department.DE)
        except Exception as e:
            raise ValueError("Invalid PythonDeveloper initialization") from e

    def work(self):
        return f"{self.name} is a python code developer"


class DataScientist(Employee):
    def __init__(self, id, name):
        try:
            super().__init__(id, name, Department.DS)
        except Exception as e:
            raise ValueError("Invalid DataScientist initialization") from e

    def work(self):
        return f"{self.name} is a Data Scientist"


e = Employee(1, 'arun', Department.DE)
print(e.id)
print(e.name)
print(e.department)
print(e.department.value)
