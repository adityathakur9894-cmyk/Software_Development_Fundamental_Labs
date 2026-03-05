# Program to display the calendar of a given month and year

# Import the calendar module
import calendar

# Take input from the user
year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))

# Display the calendar
print("\nCalendar:")
print(calendar.month(year, month))