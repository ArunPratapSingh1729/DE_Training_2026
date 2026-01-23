class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student Name: {self.name}, Marks: {self.marks}"

    def __repr__(self):
        return f"Student(name='{self.name}', marks={self.marks})"


s1 = Student("arun", 85)

print(s1)        
s1              
