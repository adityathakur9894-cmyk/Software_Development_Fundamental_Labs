class Student:
    _id_counter = 1  # Class variable for unique ID generation

    def __init__(self, name, course, attendance):
        self.student_id = Student._id_counter
        Student._id_counter += 1

        self.name = name
        self.course = course
        self.attendance = attendance

    def update_details(self, course=None, attendance=None):
        if course:
            self.course = course
        if attendance is not None:
            self.attendance = attendance

    def __str__(self):
        return (f"ID: {self.student_id}, "
                f"Name: {self.name}, "
                f"Course: {self.course}, "
                f"Attendance: {self.attendance}%")
        

class AttendanceSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, course, attendance):
        student = Student(name, course, attendance)
        self.students.append(student)
        print(f"Student added successfully! ID: {student.student_id}")

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def update_student(self, student_id, course=None, attendance=None):
        student = self.find_student(student_id)
        if student:
            student.update_details(course, attendance)
            print("Student record updated successfully.")
        else:
            print("Student not found.")

    def display_all_students(self):
        if not self.students:
            print("No student records available.")
            return

        print("\n--- Student Records ---")
        for student in self.students:
            print(student)

    def calculate_average_attendance(self):
        if not self.students:
            return 0

        total = sum(student.attendance for student in self.students)
        return total / len(self.students)


#----------- Example Usage -----------

if __name__ == "__main__":
    system = AttendanceSystem()

    # Adding students
    system.add_student("Alice", "Python Programming", 85)
    system.add_student("Bob", "Data Science", 78)

    # Display all students
    system.display_all_students()

    # Update a student
    system.update_student(1, attendance=90)

    # Display again
    system.display_all_students()

    # Calculate average attendance
    avg = system.calculate_average_attendance()
    print(f"\nAverage Attendance: {avg:.2f}%")