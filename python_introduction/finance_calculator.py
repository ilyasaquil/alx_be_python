monthly_income = float(input("Enter your monthly income:"))
monthly_expenses = float(input("Enter your monthly expenses:"))
monthly_savings = monthly_income - monthly_expenses
Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(f'Your montlhy savings are ${monthly_savings}')
print(f'Projected savings after one year, with interest, is: ${Projected_Savings}')