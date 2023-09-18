class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def display_student_info(self):
        print(f"Student Name: {self.name}")
        print(f"Student ID: {self.student_id}")


# Sample usage of the Student class
if __name__ == "__main__":
    student1 = Student("Alice", "S001")
    student2 = Student("Bob", "S002")

    student1.display_student_info()
    student2.display_student_info()
