import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from dao import orderprocessor
from entity.Model import *
from exception import *
from datetime import date

class MainProgram:
    def __init__(self):
        self.order_processor = orderprocessor.OrderProcessor()

    def display_menu(self):
        print("===== Order Management System =====")
        print("1. Create User")
        print("2. Create Product")
        print("3. Create Order")
        print("4. Cancel Order")
        print("5. Get All Products")
        print("6. Get Order by User")
        print("7. Exit")

    def create_user(self):
        user_id = int(input("Enter user ID: "))
        username = input("Enter username: ")
        password = input("Enter password: ")
        role = input("Enter role (Admin/User): ")
        user = User(user_id, username, password, role)
        self.order_processor.createUser(user)

    def create_product(self):
        # Collect user details
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        # Fetch user details from the database based on username and password
        user = self.order_processor.getUserByUsernameAndPassword(username, password)
        if user is None:
            print("Invalid username or password. User not found.")
            return
        
        # Check if the user is an admin
        if user.getRole() != "Admin":
            print("User is not authorized to create products.")
            return
        
        # Collect product details
        productId = int(input("Enter product ID: "))
        productName = input("Enter product name: ")
        description = input("Enter product description: ")
        price = float(input("Enter product price: "))
        quantityInStock = int(input("Enter quantity in stock: "))
        productType = input("Enter product type (Electronics/Clothing): ")
        
        if productType.lower() == "electronics":
            brand = input("Enter brand: ")
            warrantyPeriod = int(input("Enter warranty period: "))
            product = Electronics(productId, productName, description, price, quantityInStock, productType, brand, warrantyPeriod)
        elif productType.lower() == "clothing":
            size = input("Enter size: ")
            color = input("Enter color: ")
            product = Clothing(productId, productName, description, price, quantityInStock,productType, size , color)
        else:
            print("Invalid product type.")
            return
        
        # Pass user and product details to createProduct method
        self.order_processor.createProduct(user, product)
    
   

    def create_order(self):
        # Collect user details
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        # Fetch user details from the database based on username and password
        user = self.order_processor.getUserByUsernameAndPassword(username, password)
        if user is None:
            print("User not found. Create a new user...")
            return
            
        # Collect product details
        order_id=int(input("Enter OrderID: "))
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))
        order_date = date.today()
        
        # Create the order
        self.order_processor.createOrder(user, order_id,product_id, quantity, order_date)
        print("Order created successfully.")

    def cancel_order(self):
        # to cancel an existing order
        userId = int(input("Enter user ID: "))
        orderId = int(input("Enter order ID: "))
        
        self.order_processor.cancelOrder(userId, orderId)
        print("Order canceled successfully.")

        

    def get_all_products(self):
        # to retrieve and display all products
        products = self.order_processor.getAllProducts()
        if products:
            print("All Products:")
            for product in products:
                print("Product ID:", product.getProductId())
                print("Product Name:", product.getProductName())
                print("Description:", product.getDescription())
                print("Price:", product.getPrice())
                print("Quantity In Stock:", product.getQuantityInStock())
                print("Category:", product.getType())
                print() 
        else:
            print("No products found.")

    def get_order_by_user(self):
        # to retrieve and display orders placed by a specific user
        user_id = int(input("Enter user ID: "))
        user = User(user_id, "", "", "")  
        orders = self.order_processor.getOrderByUser(user)
        if orders:
            print(f"Orders placed by user {user_id}:")
            for order in orders:
                print("Order ID:", order[0])
                print("User ID:", order[1])
                print("Product ID:", order[2])
                print("Order Date:", order[4])
                print()  
        else:
            print(f"No orders found for user {user_id}.")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.create_product()
            elif choice == '3':
                self.create_order()
            elif choice == '4':
                self.cancel_order()
            elif choice == '5':
                self.get_all_products()
            elif choice == '6':
                self.get_order_by_user()
            elif choice == '7':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_program = MainProgram()
    main_program.run()
