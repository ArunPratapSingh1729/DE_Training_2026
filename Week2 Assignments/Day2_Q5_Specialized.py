class Employee:
    def __init__(self, emp_id, name):
        try:
            self.id = int(emp_id)
            self.name = str(name)
        except Exception as e:
            raise ValueError("Invalid Employee initialization data") from e


class HRManager(Employee):
    def __init__(self, name, emp_id):
        try:
            super().__init__(emp_id, name)
        except Exception as e:
            raise ValueError("Invalid HRManager initialization") from e
    
    def work(self):
        return f"{self.name} is managing recruitment and employee relations."


class PythonDeveloper(Employee):
    def __init__(self, name, emp_id):
        try:
            super().__init__(emp_id, name)
        except Exception as e:
            raise ValueError("Invalid PythonDeveloper initialization") from e

    def work(self):
        return f"{self.name} is a python code developer"


class DataScientist(Employee):
    def __init__(self, name, emp_id):
        try:
            super().__init__(emp_id, name)
        except Exception as e:
            raise ValueError("Invalid DataScientist initialization") from e

    def work(self):
        return f"{self.name} is a Data Scientist"


e = Employee(1, 'arun')
print(e.id)
print(e.name)
