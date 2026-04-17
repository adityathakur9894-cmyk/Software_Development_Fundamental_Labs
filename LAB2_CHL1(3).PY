# ArrowShape.py
#
# author: A. N. Other
# date: September 2016

# getting user inputs
m = int(input("Please enter the length m\n"))
u = int(input("Please enter the height u\n"))
n = int(input("Please enter the triangle side n\n"))

# calculating areas
rectangle_area = m * u
triangle_area = (n * n) / 2

total_area = rectangle_area + triangle_area

# displaying result
print("\nThe area of the arrow shape is", total_area, "\n")