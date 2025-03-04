books = int(input("Enter number of books: "))
cost_per_book = float(input("Enter cost per book: "))

order_total = books * cost_per_book

if order_total > 50:
    shipping = 0  
else:
    shipping = 25  

print("Order Total: $", order_total)
print("Shipping Charge: $", shipping)
