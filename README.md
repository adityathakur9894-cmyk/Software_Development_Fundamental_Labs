# Software_Development_Fundamental_Labs

**week6activity1.py**
Banking System (Python OOP Project)

This project is a simple Banking System developed using Object-Oriented Programming (OOP) concepts in Python. It demonstrates how classes and objects interact to perform basic banking operations like deposits and withdrawals.

 Project Structure

The system is divided into three main classes:

1️ Account Class

The Account class handles all bank account operations.

 Attributes:
account_number: Unique ID for the account
balance: Stores the current balance (default = 0)
 Methods:
deposit(amount)
Adds money to the account balance
withdraw(amount)
Deducts money if sufficient balance is available
display_balance()
Displays account number and current balance
Customer Class

The Customer class represents a bank customer.

Attributes:
name: Name of the customer
account: The account object linked to the customer
 Methods:
display_customer_info()
Displays customer name and account details
Transaction Class

The Transaction class processes banking transactions automatically.

 Attributes:
account: The account on which transaction is performed
amount: Transaction amount
transaction_type: Type of transaction ("deposit" or "withdraw")
 Method:
process_transaction()
Calls deposit() if type is "deposit"
Calls withdraw() if type is "withdraw"
Shows error if invalid type

Note: This method is automatically executed when a transaction object is created.

How the Program Works
An account is created with an initial balance.
A customer is created and linked to the account.
Customer details are displayed.
Transactions (deposit and withdraw) are performed.
Final balance is displayed.
Example Output
Customer Name: Alice
Account Number: 101
Balance: 100

50 deposited. New balance: 150
30 withdrawn. New balance: 120

Customer Name: Alice
Account Number: 101
Balance: 120
 Key Concepts Used
Classes and Objects
Encapsulation
Method Calling Between Classes
Constructor (__init__)
Basic Conditional Logic
 Conclusion

This project is a beginner-friendly example of how real-world banking systems can be modeled using Python OOP concepts. It can be further improved by adding features like transaction history, multiple accounts, or user input.

**week7lab.py**
Student Attendance System

This is a simple Python-based Student Attendance Management System that allows users to add, update, and manage student records efficiently. The system uses object-oriented programming (OOP) concepts such as classes and methods.

**Features**
Add new students with unique IDs
Update student attendance and course
Display all student records
Calculate average attendance
Code Explanation
**1. Student Class**

The Student class represents an individual student.

Key Features:

id_counter: A class variable used to generate unique student IDs automatically.
__init__: Initializes student details like name, course, and attendance.
update_attendance(): Updates the attendance percentage.
update_course(): Changes the course of the student.
display(): Returns student details in a formatted string.

How it works:
Each time a new student is created, the id_counter increases by 1, ensuring every student has a unique ID.

**2. AttendanceSystem Class**

This class manages all student records.

Key Features:

students: A list that stores all student objects.
add_student(): Creates and adds a new student to the system.
update_student(): Updates a student's attendance or course using their ID.
display_all_students(): Prints all student records.
calculate_average_attendance(): Computes the average attendance of all students.
3. Example Usage

The example at the bottom shows how the system works:

Create an instance of the system
Add students
Display all records
Update a student's attendance
Display updated records
Calculate average attendance
How the System Works
When a student is added, a unique ID is automatically assigned.
All student objects are stored in a list inside the system.
Updates are done by searching the student using their ID.
The average attendance is calculated by summing all attendance values and dividing by the number of students.
Technologies Used
Python
Object-Oriented Programming (OOP)
Example Output
Student added with ID: 1
Student added with ID: 2

ID: 1, Name: Alice, Course: Math, Attendance: 85%
ID: 2, Name: Bob, Course: Science, Attendance: 90%

Student record updated.

ID: 1, Name: Alice, Course: Math, Attendance: 95%
ID: 2, Name: Bob, Course: Science, Attendance: 90%

Average Attendance: 92.50%
