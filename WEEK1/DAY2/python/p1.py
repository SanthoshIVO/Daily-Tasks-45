from p2 import Person

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course.course_name}")

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print("Courses:", ", ".join(
            course.course_name for course in self.courses
        ) or "None")


class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []

    def enroll_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.enroll(self)

    def display_info(self):
        print(f"Course: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print("Enrolled students:",
              ", ".join(s.name for s in self.students) or "None")


# Create objects
student1 = Student("Santhosh", 22, "ST101")
student2 = Student("Alice", 20, "ST102")
course1 = Course("Python Programming", "PY101")
course2 = Course("TypeScript Fundamentals", "TS101")
course3 = Course("Data Structures", "DS101")
# Enroll the student
course1.enroll_student(student1)
course2.enroll_student(student1)
course3.enroll_student(student2)

print("\n--- Student Details ---")
student1.display_info()
print()
student2.display_info()
print("\n--- Course Details ---")
course1.display_info()

# print(dir(Student))

