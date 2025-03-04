appliance_name = input("Enter appliance name: ")
cost = float(input("Enter cost of appliance: "))

if cost > 1000:
    warranty_cost = cost * 0.10
else:
    warranty_cost = cost * 0.05

total_cost = cost + warranty_cost

print("Appliance:", appliance_name)
print("Appliance Cost: $", cost)
print("Warranty Cost: $", warranty_cost)
print("Total Cost: $", total_cost)
