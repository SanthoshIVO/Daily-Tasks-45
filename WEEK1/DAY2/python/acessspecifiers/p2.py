from p1 import Person


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)

        self.student_id = student_id   # Public
        self._courses = []             # Protected
        self.__student_id = student_id # Private

    def enroll(self, course):
        if course not in self._courses:
            self._courses.append(course)
            print(f"{self.name} enrolled in {course.course_name}")

    def get_student_id(self):
        return self.__student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.__student_id}")

        print(
            "Courses:",
            ", ".join(course.course_name for course in self._courses)
            or "None"
        )