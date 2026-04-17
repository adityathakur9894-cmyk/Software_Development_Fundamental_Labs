# Challenge 1: Print numbers 1 to n in square brackets

# Get user input
n = int(input("Enter a number n: "))

# Initialize counter
i = 1

# Loop from 1 to n
while i <= n:
    print(f"[{i}]", end=" ")  # Print in square brackets on the same line
    i += 1  # Increment counter

print()  # Move to a new line after printing all numbers