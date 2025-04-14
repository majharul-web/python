from users import Admin, Customer
from restaurant import Restaurant
from menu import Menu, MenuItem
from users import Employee


#create restaurant
mamar_bari=Restaurant("Mamar Bari")

# customer interface

def customer_interface():
    name=input("Enter your name: ")
    phone=input("Enter your phone number: ")
    email=input("Enter your email: ")
    address=input("Enter your address: ")
    
    customer=Customer(name=name, phone=phone, email=email, address=address)
    print("Welcome to the restaurant!")
    
    while True:
        print("1. View Menu")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")
        
        choice=int(input("Enter your choice: "))
        if choice==1:
            customer.view_menu(mamar_bari)
        elif choice==2:
            item_name=input("Enter item name to add to cart: ")
            quantity=int(input("Enter quantity: "))
            customer.add_to_cart(mamar_bari, item_name, quantity)
        elif choice==3:
            customer.view_cart()
        elif choice==4:
            customer.pay_bill()
        elif choice==5:
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice! Please try again.")


# admin interface

def admin_interface():
    name=input("Enter your name: ")
    phone=input("Enter your phone number: ")
    email=input("Enter your email: ")
    address=input("Enter your address: ")
    
    admin=Admin(name=name, phone=phone, email=email, address=address)
    print("Welcome Admin!")
    
    while True:
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Add Menu Item")
        print("4. View Menu")
        print("5. Remove Menu Item")
        print("6. Exit")
   
        choice=int(input("Enter your choice: "))
        if choice==1:
            # Add employee functionality
            name=input("Enter employee name: ")
            phone=input("Enter employee phone number: ")
            email=input("Enter employee email: ")
            address=input("Enter employee address: ")
            age=int(input("Enter employee age: "))
            designation=input("Enter employee designation: ")
            salary=float(input("Enter employee salary: "))
            
            employee=Employee(name, phone, email, address, age, designation, salary)
            admin.add_employee(mamar_bari, employee)
            print("Employee added successfully!")
        elif choice==2:
            admin.view_employee(mamar_bari)
        elif choice==3:
            item_name=input("Enter item name: ")
            price=float(input("Enter item price: "))
            quantity=int(input("Enter item quantity: "))
            item=MenuItem(item_name, price, quantity)
            admin.add_menu_item(mamar_bari, item)
        elif choice==4:
            admin.view_menu(mamar_bari)
        elif choice==5:
            item_name=input("Enter item name to remove: ")
            admin.remove_item(mamar_bari, item_name)
        elif choice==6:
            print("Thank you for using the admin interface!")
            break
        else:
            print("Invalid choice! Please try again.")



# Main function
while True:
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        customer_interface()
    elif choice==2:
        admin_interface()
    elif choice==3:
        print("Exiting the program!")
        break
    else:
        print("Invalid choice! Please try again.")


    
    
# This is the main entry point of the program. It allows the user to choose between customer and admin interfaces.
# The customer can view the menu, add items to the cart, view the cart, and pay the bill.
# The admin can add employees, view employees, add menu items, view the menu, and remove menu items.
# The program continues to run until the user chooses to exit.
# The customer and admin interfaces are implemented in separate functions for better organization and readability.
# The main function serves as the entry point for the program, allowing users to choose between customer and admin interfaces.
# The program is designed to be user-friendly and provides clear instructions for each action.
# The code is structured to allow for easy expansion and modification in the future.

    