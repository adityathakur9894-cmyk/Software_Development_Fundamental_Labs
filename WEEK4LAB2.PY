registration_counter = 50000
def student_registration():
    global registration_counter
    registration_id = registration_counter
    registration_counter += 1
    date = input("Enter the registration date (dd/mm/yyyy): ")
    student_id = input("Enter the Student ID: ")
    student_name = input("Enter the Student Name: ")
    course_name = input("Enter the Course Name: ")
    return date, student_id, student_name, course_name, registration_id
date, student_id, student_name, course_name, registration_id = student_registration()
print("\nStudent Registration Information:")
print("Date:", date)
print("Student ID:", student_id)
print("Student Name:", student_name)
print("Course Name:", course_name)
print("Registration ID:", registration_id)