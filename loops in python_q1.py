# Initialize variables
number = 100
sum_even = 0

# Iterate through numbers from 100 to 200
while number <= 200:
    # Check if the number is even
    if number % 2 == 0:
        # Add the even number to the sum
        sum_even += number
    # Move to the next number
    number += 1

# Output the sum of even numbers
print("Sum of even numbers between 100 and 200:", sum_even)
