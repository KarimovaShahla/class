class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return [student.name for student in self.students]


class Student:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def registration(self, course):
        self.courses.append(course)
        course.add_student(self)

    def get_courses(self):
        return [course.name for course in self.courses]


course1 = Course("Math")
course2 = Course("Physics")

student1 = Student("Lisa")
student2 = Student("Murad")

student1.registration(course1)
student1.registration(course2)

student2.registration(course1)

print(f"{student1.name} registered courses: {student1.get_courses()}")
print(f"{student2.name} registered courses: {student2.get_courses()}")

print(f"{course1.name} students: {course1.get_students()}")
print(f"{course2.name} students: {course2.get_students()}")
