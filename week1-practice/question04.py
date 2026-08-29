# QUESTION 04

# Function to calculate total amount, discount, and final amount
def calculate_bill(unit_price, quantity):
    total_amount = unit_price * quantity

    if total_amount >= 2000:
        discount = total_amount * 0.10
    else:
        discount = 0

    final_amount = total_amount - discount

    return total_amount, discount, final_amount

# Take input from the user
product_name = input()
unit_price = int(input())
quantity = int(input())

total_amount, discount, final_amount = calculate_bill(unit_price, quantity)

# Print the results
print(f"Product Name: {product_name}")
print(f"Price: {unit_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total Amount: {total_amount:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Final Amount: {final_amount:.2f}")