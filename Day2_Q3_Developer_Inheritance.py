class Employee():
      
     def __init__(self,id,name,department):
        self.id = id
        self.name = name
        self.department = department

class Developer(Employee):
    
    def projectassigned(self,project_name = None):
        self.project_name = project_name
        print(f"The project name is {self.project_name}")

    def developerinfo(self):
        print("The Id of the Developer is : ")
        print("The name of the Developer is : ")
        print("The department of the Developer is : ")
        if self.project_name:
        print("The Project of the Developer is : ")


developer1 = Developer(1,'arun','data engineering')
developer1.projectassigned("DE Project")
developer1.developerinfo()
