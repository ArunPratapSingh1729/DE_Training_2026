class Employee():
      
     def __init__(self,name,id,department):
        self.name = name
        self.id = id
        self.department = department

emp1 = Employee('rahul',1,'data science')
emp2 = Employee('arun',2,'data engineering')

print("Employee id :", emp1.id)
print("Employee name :" , emp2.name)
