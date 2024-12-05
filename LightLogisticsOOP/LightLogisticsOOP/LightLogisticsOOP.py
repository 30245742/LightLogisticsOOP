from abc import ABC, abstractmethod  # Importing the Abstract Base Class (ABC) module and abstractmethod decorator

class DatabaseHandler(ABC):  # Defining an abstract base class for database operations
    @abstractmethod
    def connect(self):  # Abstract method for establishing a connection to the database
        pass

    @abstractmethod
    def execute_query(self, query, params=None):  # Abstract method for executing a query, with optional parameters
        pass

    @abstractmethod
    def close(self):  # Abstract metod for closing the database connection
        pass

class SQLFileHandler(DatabaseHandler):  # A concrete implementation of DatabaseHandler for handling SQL files
    def __init__(self, filename='inventory.sql'):
        # Initialize the handler with a default file name and set up attributes
        self.filename = filename
        self.file = None

    def connect(self):
        # Open the .sql file in write mode and create the products table if it doesn't exist
        self.file = open(self.filename, 'w')
        print(f"Opened SQL file '{self.filename}' for writing.")
        self.create_table()

    def create_table(self):
        # Define and execute the SQL query to create the products table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        );
        '''
        self.execute_query(create_table_query)

    def execute_query(self, query, params=None):
        # Process the SQL query and write it to the file, formatting parameters if provided
        if params:
            query_formatted = query
            for param in params:
                if isinstance(param, str):
                    param_str = "'" + param.replace("'", "''") + "'"
                elif param is None:
                    param_str = 'NULL'
                else:
                    param_str = str(param)
                query_formatted = query_formatted.replace('?', param_str, 1)
        else:
            query_formatted = query

        self.file.write(query_formatted.strip() + '\n')

    def close(self):
        # Close the SQL file if it is open
        if self.file:
            self.file.close()
            print(f"Closed SQL file '{self.filename}'.")

class Product:  # Represents a product with properties for id, name, quantity, and price
    def __init__(self, product_id, name, quantity, price):
        # Initialize the product with private attributes and set initial values
        self.__product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    @property
    def product_id(self):
        # Read-only property for the product ID
        return self.__product_id

    @property
    def name(self):
        # Property to get the product name
        return self.__name

    @name.setter
    def name(self, value):
        # Setter to update the product name
        self.__name = value

    @property
    def quantity(self):
        # Property to get the product quantity
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        # Setter to update the quantity, ensuring it is not negative
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = value

    @property
    def price(self):
        # Property to get the product price
        return self.__price

    @price.setter
    def price(self, value):
        # Setter to update the price, ensuring it is not negative
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value

        #User interface
def main_menu(inv_manager):
    try:
        while True:
            print("\nInventory Management System")
            print("1. Add Product")
            print("2. Update Product")
            print("3. Remove Product")
            print("4. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                try:
                    product_id = int(input("Product ID: "))
                    name = input("Name: ")
                    quantity = int(input("Quantity: "))
                    price = float(input("Price: "))
                    product = Product(product_id, name, quantity, price)
                    inv_manager.add_product(product)
                except ValueError as e:
                    print(f"Invalid input: {e}")
            elif choice == '2':
                try:
                    product_id = int(input("Product ID to update: "))
                    print("Leave fields blank to keep current values.")
                    name = input("New Name: ")
                    quantity_input = input("New Quantity: ")
                    price_input = input("New Price: ")
                    kwargs = {}
                    if name:
                        kwargs['name'] = name # Add the name to the keyword arguments if provided
                    if quantity_input:
                        kwargs['quantity'] = int(quantity_input)
                    if price_input:
                        kwargs['price'] = float(price_input) # Convert the price input to a float and add it to kwargs
                    inv_manager.update_product(product_id, **kwargs)
                except ValueError as e:
                    print(f"Invalid input: {e}")
            elif choice == '3':
                try:
                    product_id = int(input("Product ID to remove: "))
                    inv_manager.remove_product(product_id)
                except ValueError as e:
                    print(f"Invalid input: {e}")
            elif choice == '4':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        inv_manager.close()

if __name__ == "__main__":
    db_handler = SQLFileHandler()
    inv_manager = InventoryManager(db_handler)
    main_menu(inv_manager)
