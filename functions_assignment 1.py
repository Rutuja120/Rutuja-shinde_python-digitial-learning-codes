#define initial size of loan, duration of loan, and annual interest rate
def compute_monthly_payment(loan_amount, years, annual_interest_rate):
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    # Convert years to months
    months = years * 12
    
    # Compute monthly payment using the formula
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)
    
    return monthly_payment

def main():
    
    loan_amount = float(input("Enter the loan amount: $"))
    years = int(input("Enter the number of years: "))
    annual_interest_rate = float(input("Enter the annual interest rate (%): "))
    
    
    monthly_payment = compute_monthly_payment(loan_amount, years, annual_interest_rate)
    
  
    print("Monthly payment: $", round(monthly_payment, 2))

if __name__ == "__main__":
    main()


