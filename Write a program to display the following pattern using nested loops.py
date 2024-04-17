# Define the number of rows
rows = 5

# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for columns
    for j in range(1, i + 1):
        # Print the current row number 'i' without newline
        print(i, end="")
    # Move to the next line after each row is printed
    print()
