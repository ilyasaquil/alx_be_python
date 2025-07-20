# pattern_drawing.py

# Prompt user for size of the pattern
size = int(input("Enter the size of the pattern: "))

# Ensure size is positive
if size <= 0:
    print("Please enter a positive integer.")
else:
    row = 0
    # While loop for rows
    while row < size:
        # For loop for columns
        for col in range(size):
            print("*", end="")
        print()  # Move to the next line after each row
        row += 1
