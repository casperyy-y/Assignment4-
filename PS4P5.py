last_name = input("Enter last name: ")
dependents = int(input("Enter number of dependents: "))
gross_income = float(input("Enter gross income: "))

adjusted_income = gross_income - (12000 * dependents)

if adjusted_income > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

tax = adjusted_income * tax_rate

if tax < 100:
    tax = 100

print("Last Name:", last_name)
print("Gross Income: $", gross_income)
print("Number of Dependents:", dependents)
print("Adjusted Income: $", adjusted_income)
print("Income Tax: $", tax)
