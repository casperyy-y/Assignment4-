item = input("Enter item type (A or B): ").strip().upper()
quantity = int(input("Enter quantity: "))

if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00  # Assume any other entry is B

extended_price = quantity * unit_price

print("Item:", item)
print("Unit Price: $", unit_price)
print("Extended Price: $", extended_price)
