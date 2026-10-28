
class Person {
    constructor(
        public name: string,
        public age: number
    ) {}

    displayInfo(): void {
        console.log(`Name: ${this.name}`);
        console.log(`Age: ${this.age}`);
    }
}

class Student extends Person {
    private courses: Course[] = [];

    constructor(
        name: string,
        age: number,
        public studentId: string
    ) {
        super(name, age);
    }

    enroll(course: Course): void {
        if (!this.courses.includes(course)) {
            this.courses.push(course);
            console.log(
                `${this.name} enrolled in ${course.courseName}`
            );
        }
    }

    getCourses(): Course[] {
        return [...this.courses];
    }

    override displayInfo(): void {
        super.displayInfo();
        console.log(`Student ID: ${this.studentId}`);
        console.log(
            "Courses:",
            this.courses.map(c => c.courseName).join(", ") || "None"
        );
    }
}

class Course {
    private students: Student[] = [];

    constructor(
        public courseName: string,
        public courseCode: string
    ) {}

    enrollStudent(student: Student): void {
        if (!this.students.includes(student)) {
            this.students.push(student);
            student.enroll(this);
        }
    }

    displayInfo(): void {
        console.log(`Course: ${this.courseName}`);
        console.log(`Course Code: ${this.courseCode}`);
        console.log(
            "Enrolled students:",
            this.students.map(s => s.name).join(", ") || "None"
        );
    }
}

// Create objects
const student1 = new Student("Santhosh", 22, "ST101");
const student2 = new Student("Alice", 20, "ST102");
const student3 = new Student("Bob", 21, "ST103");
const course1 = new Course("Python Programming", "PY101");
const course2 = new Course("TypeScript Fundamentals", "TS101");

// Enroll the student
course1.enrollStudent(student1);
course2.enrollStudent(student1);

console.log("\n--- Student Details ---");
student1.displayInfo();

console.log("\n--- Course Details ---");
course1.displayInfo();
