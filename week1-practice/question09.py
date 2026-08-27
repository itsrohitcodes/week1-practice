class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def is_bulk_order(self):
        return self.quantity >= 10

    def __str__(self):
        return (
            f"Product Name: {self.product_name}\n"
            f"Price: {self.price:.2f}\n"
            f"Quantity: {self.quantity}\n"
            f"Total Amount: {self.calculate_total():.2f}"
    )


product_name = input()
price = int(input())
quantity = int(input())

product = Product(product_name, price, quantity)

print(product)
if product.is_bulk_order():
    print("Order Type: Bulk Order")
else:
    print("Order Type: Regular Order")