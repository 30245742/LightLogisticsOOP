from abc import ABC, abstractmethod

class DatabaseHandler(ABC):  # Abstraction
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

class SQLiteHandler(DatabaseHandler):  # Polymorphism
    def connect(self):
        # Code to connect to SQLite database
        print("Connecting to SQLite database.")

    def execute_query(self, query):
        # Code to execute query
        print(f"Executing query: {query}")

class Product:
    # Same as before
    pass

class InventoryManager:
    def __init__(self, db_handler):
        self.products = {}
        self.db_handler = db_handler
        self.db_handler.connect()

    def add_product(self, product):
        self.products[product.get_product_id()] = product
        self.db_handler.execute_query("INSERT INTO products VALUES (...)")

# Usage Example
if __name__ == "__main__":
    db_handler = SQLiteHandler()
    inv_manager = InventoryManager(db_handler)
    # Add products as before
