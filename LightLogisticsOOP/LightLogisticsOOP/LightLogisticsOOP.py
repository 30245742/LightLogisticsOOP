class Product:
    def __init__(self, product_id, name, quantity, price):
        self.__product_id = product_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    @property  # Getter for name
    def name(self):
        return self.__name

    @name.setter  # Setter for name
    def name(self, value):
        self.__name = value

    # Similar getters and setters for other attributes

    def get_product_id(self):
        return self.__product_id

class InventoryManager:
    def __init__(self, db_handler):
        self.products = {}
        self.db_handler = db_handler
        self.db_handler.connect()

    def add_product(self, product):
        self.products[product.get_product_id()] = product
        self.db_handler.execute_query("INSERT INTO products VALUES (...)")

    def update_product(self, product_id, **kwargs):
        # Update product details
        pass

    def remove_product(self, product_id):
        # Remove product from inventory
        pass

def main_menu():
    print("Welcome to the Inventory Management System")
    # Display options to the user
    # Get user input and perform actions

# Usage Example
if __name__ == "__main__":
    db_handler = SQLiteHandler()
    inv_manager = InventoryManager(db_handler)
    main_menu()
