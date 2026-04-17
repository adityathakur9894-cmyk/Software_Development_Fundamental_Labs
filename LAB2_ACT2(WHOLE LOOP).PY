# Challenge 3: Print multiples of p from 10 to q using a while loop

# Get user input
p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))

# Find the first multiple of p that is >= 10
num = ((10 + p - 1) // p) * p  # Ceiling division to get first multiple

# Loop through multiples until we exceed q
while num <= q:
    print(num, end=", ")
    num += p  # Go to the next multiple