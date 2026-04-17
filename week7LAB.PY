class Student:
    id_counter = 1  # Class variable for unique ID

    def __init__(self, name, course, attendance):
        self.student_id = Student.id_counter
        Student.id_counter += 1
        self.name = name
        self.course = course
        self.attendance = attendance

    def update_attendance(self, new_attendance):
        self.attendance = new_attendance

    def update_course(self, new_course):
        self.course = new_course

    def display(self):
        return f"ID: {self.student_id}, Name: {self.name}, Course: {self.course}, Attendance: {self.attendance}%"


class AttendanceSystem:
    def __init__(self):
        self.students = []  # List to store student objects

    def add_student(self, name, course, attendance):
        student = Student(name, course, attendance)
        self.students.append(student)
        print(f"Student added with ID: {student.student_id}")

    def update_student(self, student_id, attendance=None, course=None):
        for student in self.students:
            if student.student_id == student_id:
                if attendance is not None:
                    student.update_attendance(attendance)
                if course is not None:
                    student.update_course(course)
                print("Student record updated.")
                return
        print("Student not found.")

    def display_all_students(self):
        if not self.students:
            print("No records found.")
        for student in self.students:
            print(student.display())

    def calculate_average_attendance(self):
        if not self.students:
            print("No data available.")
            return 0
        total = 0
        for student in self.students:
            total += student.attendance
        average = total / len(self.students)
        return average


# ----------------------------
# Example Usage
# ----------------------------
system = AttendanceSystem()

# Adding students
system.add_student("Alice", "Math", 85)
system.add_student("Bob", "Science", 90)

# Display records
system.display_all_students()

# Update student
system.update_student(1, attendance=95)

# Display updated records
system.display_all_students()

# Calculate average attendance
avg = system.calculate_average_attendance()
print(f"Average Attendance: {avg:.2f}%")