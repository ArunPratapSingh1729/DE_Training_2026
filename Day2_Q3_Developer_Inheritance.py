class Employee():
      
    def __init__(self,id,name,department):
        try:
            self.id = int(id)
            self.name = str(name)
            self.department = str(department)
        except Exception as e:
            raise ValueError("Invalid Employee data") from e


class Developer(Employee):
    
    def projectassigned(self,project_name = None):
        try:
            self.project_name = project_name
            print(f"The project name is {self.project_name}")
        except Exception as e:
            print("Error while assigning project:", e)


    def developerinfo(self):
        print(f"The Id of the Developer is : {self.id}")
        print(f"The name of the Developer is : {self.name}")
        print(f"The department of the Developer is : {self.department}")
        if self.project_name:
            print(f"The Project of the Developer is : {self.project_name}")


developer1 = Developer(1,'arun','data engineering')
developer1.projectassigned("DE Project")
developer1.developerinfo()
