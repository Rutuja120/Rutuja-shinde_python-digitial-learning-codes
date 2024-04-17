def calculate_simple_interest(p, n, r):
    # Calculate simple interest
    interest = (p * n * r) / 100
    return interest

# Receive input from the user for 3 sets of values
for i in range(3):
    print(f"Set {i + 1}:")
    p = float(input("Enter principal amount (p): "))
    n = float(input("Enter time period (n) in years: "))
    r = float(input("Enter rate of interest (r) in percentage: "))
    
    # Calculate simple interest for the current set of values
    si = calculate_simple_interest(p, n, r)
    
    # Display the result
    print(f"Simple interest for set {i + 1}: {si}")
    print()
