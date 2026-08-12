# Function-Based Shopping bill calculator

def calculate_bill(price, quantity):
    total_amount = price * quantity

    if total_amount >= 2000:
        discount = total_amount * 0.10
    else:
        discount = 0

    final_amount = total_amount - discount
    return total_amount, discount, final_amount

product_name = input()
price = float(input())
quantity = int(input())

total_amount, discount, final_amount = calculate_bill(price, quantity)

print("Product Name:", product_name)
print("Price:", price)
print("Quantity:", quantity)
print("Total Amount:", total_amount)
print("Discount:", discount)
print("Final Amount:", final_amount)