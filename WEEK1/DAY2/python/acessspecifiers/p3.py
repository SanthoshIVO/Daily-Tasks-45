from p2 import Student


class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name  # Public
        self._course_code = course_code # Protected
        self.__students = []            # Private

    def enroll_student(self, student):
        if student not in self.__students:
            self.__students.append(student)
            student.enroll(self)

    def get_course_code(self):
        return self._course_code

    def display_info(self):
        print(f"Course: {self.course_name}")
        print(f"Course Code: {self._course_code}")

        print(
            "Enrolled students:",
            ", ".join(student.name for student in self.__students)
            or "None"
        )


# Create students
student1 = Student("Santhosh", 22, "ST101")
student2 = Student("Alice", 20, "ST102")

# Create courses
course1 = Course("Python Programming", "PY101")
course2 = Course("TypeScript Fundamentals", "TS101")
course3 = Course("Data Structures", "DS101")

# Enroll students
course1.enroll_student(student1)
course2.enroll_student(student1)
course3.enroll_student(student2)

# Display student details
print("\n--- Student Details ---")
student1.display_info()

print()
student2.display_info()

# Display course details
print("\n--- Course Details ---")
course1.display_info()
course2.display_info()
course3.display_info()

# Demonstrate access specifiers
print("\n--- Access Specifiers ---")

# Public
print("Public name:", student1.name)
print("Public student ID:", student1.student_id)

# Protected (accessible, but intended for internal use)
print("Protected age:", student1._age)
print("Protected course code:", course1._course_code)

# Private (access through methods)
print("Private student ID:", student1.get_student_id())
print("Private email:", student1.get_email())

# Inspect class attributes
print("\n--- Student Class Attributes ---")
print(dir(Student))