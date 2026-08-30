# question 09

# class product
class Product:
    # product details
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    # Calculates total amount
    def calculate_total(self):
        return self.price * self.quantity

    # Checks if the order is bulk
    def is_bulk_order(self):
        return self.quantity >= 10

    # String representation
    def __str__(self):
        return (
            f"Product Name: {self.product_name}\n"
            f"Price: {self.price:.2f}\n"
            f"Quantity: {self.quantity}\n"
            f"Total Amount: {self.calculate_total():.2f}"
    )

# Inputs from user
product_name = input()
price = int(input())
quantity = int(input())

# Function call
product = Product(product_name, price, quantity)

# Print the results
print(product)
if product.is_bulk_order():
    print("Order Type: Bulk Order")
else:
    print("Order Type: Regular Order")