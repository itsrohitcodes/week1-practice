class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def is_bulk_order(self):
        return self.quantity >= 10

    def get_order_type(self):
        if self.is_bulk_order():
            return "Bulk Order"
        return "Regular Order"

    def __str__(self):
        return f"Product Name: {self.product_name}"


# Take input from user
product_name = input("Enter product name: ")
price = int(input("Enter price: "))
quantity = int(input("Enter quantity: "))

product = Product(product_name, price, quantity)

# Display details
print(product)
print(f"Price: ₹{product.price}")
print(f"Quantity: {product.quantity}")
print(f"Total Amount: ₹{product.calculate_total()}")
print(f"Order Type: {product.get_order_type()}")