quantity = int(input("Enter quantity of item: "))

if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

extended_price = quantity * unit_price
tax = extended_price * 0.07
total = extended_price + tax

print("Quantity:", quantity)
print("Unit Price: $", unit_price)
print("Extended Price: $", extended_price)
print("Tax: $", round(tax, 2))
print("Total: $", round(total, 2))
