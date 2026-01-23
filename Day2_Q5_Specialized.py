class Employee:
    def __init__(self, emp_id, name):
        self.id = emp_id
        self.name = name


class HRManager(Employee):
    def __init__(self, name, emp_id):
        super().__init__(emp_id, name)
    
    def work(self):
        return f"{self.name} is managing recruitment and employee relations."


class PythonDeveloper(Employee):
    def __init__(self, name, emp_id):
        super().__init__(emp_id, name)

    def work(self):
        return f"{self.name} is a python code developer"


class DataScientist(Employee):
    def __init__(self, name, emp_id):
        super().__init__(emp_id, name)

    def work(self):
        return f"{self.name} is a Data Scientist"


e = Employee(1, 'arun')
print(e.id)
print(e.name)
