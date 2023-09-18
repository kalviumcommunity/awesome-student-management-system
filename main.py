# This file demonstrates the use of the "this" pointer in Python within class methods.

from student import Student

if __name__ == "__main__":
    student1 = Student("Alice", "S001")
    student2 = Student("Bob", "S002")

    # Using "this" pointer within the class method
    student1.display_student_info()
    student2.display_student_info()
