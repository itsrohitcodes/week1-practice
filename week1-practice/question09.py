# Create Product class

class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def is_bulk_order(self):
        if self.quantity >= 10:
            return True
        else:
            return False

    def __str__(self):
        return "Product Name: " + self.product_name

# Take input from user
product_name = input()
price = int(input())
quantity = int(input())

product = Product(product_name, price, quantity)

total_amount = product.calculate_total()

if product.is_bulk_order():
    order_type = "Bulk Order"
else:
    order_type = "Regular Order"

# Display details
print(product)
print(f"Price: {product.price}")
print(f"Quantity: {product.quantity}")
print(f"Total Amount: {total_amount}")
print(f"Order Type: {order_type}")