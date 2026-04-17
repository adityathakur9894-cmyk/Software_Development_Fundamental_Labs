# CompoundShape2.py
#
# Author: A. N. Other
# Date: September 2016
# Description: Program to calculate the area of a compound L-shaped figure

# Get user inputs
a = int(input("Please enter the length of a: "))
b = int(input("Please enter the length of b: "))

# Calculate the two rectangular areas
area1 = a * b      # vertical rectangle
area2 = a * a      # bottom square

# Total area of the compound shape
total_area = area1 + area2

# Print the result
print("The area of your shape is", total_area)

# Testing
'''
Expected results:
a = 1, b = 4  -> Output = 5
a = 3, b = 13 -> Output = 48
'''