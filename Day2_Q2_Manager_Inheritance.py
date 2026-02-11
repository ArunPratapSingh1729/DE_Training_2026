class Employee:
      
    def __init__(self, id, name, department):
        try:
            self.id = int(id)
            self.name = str(name)
            self.department = str(department)
        except Exception as e:
            print("Error while initializing Employee:", e)

        
    def info(self):
        print("Id of the manager is :", self.id)
        print("Name of the manager is :", self.name)
        print("Department of the manager is :", self.department)


class Manager(Employee):
    def __init__(self, id, name, department):
        try:
            super().__init__(id, name, department)
        except Exception as e:
            print("Error while initializing Manager:", e)

    def work(self):
        return f"{self.name} is managing recruitment and employee relations."


manager1 = Manager(11, 'arun', 'data engineering')
print(manager1.id)
print(manager1.name)
print(manager1.department)
