class Product:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id  # Encapsulation
        self.name = name
        self.quantity = quantity
        self.price = price

class InventoryManager:
    def __init__(self):
        self.products = {}  # Using a dictionary to store products

    def add_product(self, product):
        self.products[product.product_id] = product

# Usage Example
if __name__ == "__main__":
    inv_manager = InventoryManager()
    prod = Product(1, "Widget", 100, 2.99)
    inv_manager.add_product(prod)

