def calculate_bill(unit_price, quantity):
    total_amount = unit_price * quantity

    if total_amount >= 2000:
        discount = total_amount * 0.10
    else:
        discount = 0

    final_amount = total_amount - discount

    return total_amount, discount, final_amount


product_name = input("Enter product name: ")
unit_price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total_amount, discount, final_amount = calculate_bill(unit_price, quantity)

print("\n----- Shopping Bill -----")
print("Product Name:", product_name)
print(f"Price: ₹{unit_price:.2f}")
print("Quantity:", quantity)
print(f"Total Amount: ₹{total_amount:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Amount: ₹{final_amount:.2f}")