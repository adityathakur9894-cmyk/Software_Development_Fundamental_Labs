# CompoundShape_U.py
#
# author: A. N. Other
# date: September 2016

# getting user inputs
s = int(input("Please enter the length of s\n"))
g = int(input("Please enter the height g\n"))
q = int(input("Please enter the inner width q\n"))
w = int(input("Please enter the inner height w\n"))

# calculating areas
outer_area = s * g
inner_area = q * w

total_area = outer_area - inner_area

# displaying result
print("\nThe area of the compound shape is", total_area, "\n")