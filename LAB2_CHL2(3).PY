# Shape3.py

import math

# getting user inputs
g = float(input("Enter the height (g): "))
e = float(input("Enter the rectangle width (e): "))
f = float(input("Enter the triangle base (f): "))

# semicircle
r = g / 2
semi_circle = 0.5 * math.pi * r**2

# rectangle
rectangle = e * g

# triangle
triangle = 0.5 * f * g

# total area
total_area = semi_circle + rectangle + triangle

print("\nThe area of Shape 3 is:", total_area)