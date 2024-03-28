# https://www.codewars.com/kata/563f037412e5ada593000114/solutions/python

def calculate_years(principal, interest, tax, desired):
    years = 0


    while principal < desired:
        acc_interest = principal * interest
        tax_amount = (acc_interest * tax)
        principal += acc_interest - tax_amount
        years += 1

    return years

print(calculate_years(1000, 0.05, 0.18, 1100))
        
