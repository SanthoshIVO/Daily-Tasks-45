"use strict";
class Person {
    name;
    age;
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    displayInfo() {
        console.log(`Name: ${this.name}`);
        console.log(`Age: ${this.age}`);
    }
}
class Student extends Person {
    studentId;
    courses = [];
    constructor(name, age, studentId) {
        super(name, age);
        this.studentId = studentId;
    }
    enroll(course) {
        if (!this.courses.includes(course)) {
            this.courses.push(course);
            console.log(`${this.name} enrolled in ${course.courseName}`);
        }
    }
    getCourses() {
        return [...this.courses];
    }
    displayInfo() {
        super.displayInfo();
        console.log(`Student ID: ${this.studentId}`);
        console.log("Courses:", this.courses.map(c => c.courseName).join(", ") || "None");
    }
}
class Course {
    courseName;
    courseCode;
    students = [];
    constructor(courseName, courseCode) {
        this.courseName = courseName;
        this.courseCode = courseCode;
    }
    enrollStudent(student) {
        if (!this.students.includes(student)) {
            this.students.push(student);
            student.enroll(this);
        }
    }
    displayInfo() {
        console.log(`Course: ${this.courseName}`);
        console.log(`Course Code: ${this.courseCode}`);
        console.log("Enrolled students:", this.students.map(s => s.name).join(", ") || "None");
    }
}
// Create objects
const student1 = new Student("Santhosh", 22, "ST101");
const student2 = new Student("Alice", 20, "ST102");
const course1 = new Course("Python Programming", "PY101");
const course2 = new Course("TypeScript Fundamentals", "TS101");
// Enroll the student
course1.enrollStudent(student1);
course2.enrollStudent(student1);
course2.enrollStudent(student2);
console.log("\n--- Student Details ---");
student1.displayInfo();
console.log("\n--- Course Details ---");
course1.displayInfo();
