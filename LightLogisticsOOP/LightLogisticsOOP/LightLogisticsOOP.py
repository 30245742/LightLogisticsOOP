import sqlite3
from abc import ABC, abstractmethod

class DatabaseHandler(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

class SQLiteHandler(DatabaseHandler):
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect('inventory.db')
        self.cursor = self.connection.cursor()
        print("Connected to SQLite database.")

    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

class Product:
    def __init__(self, product_id, name, quantity, price):
        self.__product_id = product_id
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    # Additional getters and setters...

    def get_product_id(self):
        return self.__product_id

class PerishableProduct(Product):
    def __init__(self, product_id, name, quantity, price, expiration_date):
        super().__init__(product_id, name, quantity, price)
        self.expiration_date = expiration_date

class InventoryManager:
    def __init__(self, db_handler):
        self.products = {}
        self.db_handler = db_handler
        self.db_handler.connect()

    def add_product(self, product):
        self.products[product.get_product_id()] = product
        query = "INSERT INTO products (id, name, quantity, price) VALUES (?, ?, ?, ?)"
        params = (
            product.get_product_id(),
            product.name,
            product.quantity,
            product.price
        )
        self.db_handler.execute_query(query, params)

    def update_product(self, product_id, **kwargs):
        product = self.products.get(product_id)
        if not product:
            print("Product not found.")
            return
        for key, value in kwargs.items():
            setattr(product, key, value)
        # Update database

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
            query = "DELETE FROM products WHERE id = ?"
            params = (product_id,)
            self.db_handler.execute_query(query, params)
        else:
            print("Product not found.")

def main_menu(inv_manager):
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Remove Product")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            product_id = int(input("Product ID: "))
            name = input("Name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            product = Product(product_id, name, quantity, price)
            inv_manager.add_product(product)
        elif choice == '2':
            product_id = int(input("Product ID to update: "))
            name = input("New Name (leave blank to keep current): ")
            kwargs = {}
            if name:
                kwargs['name'] = name
            inv_manager.update_product(product_id, **kwargs)
        elif choice == '3':
            product_id = int(input("Product ID to remove: "))
            inv_manager.remove_product(product_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    db_handler = SQLiteHandler()
    inv_manager = InventoryManager(db_handler)
    main_menu(inv_manager)
