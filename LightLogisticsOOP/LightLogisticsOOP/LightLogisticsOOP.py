class Product:
    def __init__(self, product_id, name, quantity, price):
        self.__product_id = product_id  # Private attribute
        self.name = name
        self.quantity = quantity
        self.price = price

    def get_product_id(self):  # Encapsulation via getter
        return self.__product_id

class PerishableProduct(Product):  # Inheritance
    def __init__(self, product_id, name, quantity, price, expiration_date):
        super().__init__(product_id, name, quantity, price)
        self.expiration_date = expiration_date

class InventoryManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.get_product_id()] = product

# Usage Example
if __name__ == "__main__":
    inv_manager = InventoryManager()
    perishable = PerishableProduct(2, "Milk", 50, 1.99, "2023-12-31")
    inv_manager.add_product(perishable)
