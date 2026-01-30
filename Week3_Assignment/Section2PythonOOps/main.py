class Student:
    def __init__(self, student_id, name):
        self._student_id = student_id
        self._name = name
        self._courses_enrolled = []

    def enroll_course(self, course):
        if course in self._courses_enrolled:
            return

        course.enroll_student(self)

    def __repr__(self):
        return f"Student({self._student_id}, {self._name})"


class Course:
    def __init__(self, course_code, course_name, max_students):
        self._course_code = course_code
        self._course_name = course_name
        self._max_students = max_students
        self._students_enrolled = []

    def enroll_student(self, student):
        if len(self._students_enrolled) >= self._max_students:
            return  

        if student in self._students_enrolled:
            return  

        self._students_enrolled.append(student)
        student._courses_enrolled.append(self)

    def get_enrolled_students(self):
        return [student._name for student in self._students_enrolled]

    def __str__(self):
        return f"Course name: {self._course_name}, Course id: {self._course_code}"

    def __repr__(self):
        return f"Course({self._course_code}, {self._course_name})"


class University:
    def __init__(self):
        self.students = []
        self.courses = []

    def register_student(self, student):
        self.students.append(student)

    def offer_course(self, course):
        self.courses.append(course)

    def get_students_by_course(self, course_code):
        for course in self.courses:
            if course._course_code == course_code:
                return course.get_enrolled_students()
        return []
