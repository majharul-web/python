from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart=Order()
    
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()
        
    def add_to_cart(self,restaurant,item_name,quantity):
        item=restaurant.menu.find_item(item_name)
        if item:
            if quantity>item.quantity:
                print("Quantity not available")
                return
            item.quantity=quantity
            self.cart.add_item(item)
            print("Item added to cart successfully!")
        else:
            print("Item not found")
            
    def view_cart(self):
        print("Cart Items")
        print("Name\tPrice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print("Total Price:", self.cart.calculate_total)

    
class Order:
    def __init__(self):
        self.items={}
    
    def add_item(self,item):
        if item in self.items:
            self.items[item]+=item.quantity
        else:
            self.items[item]=item.quantity
        
    
    def remove_item(self,item):
        if item in self.items:
            del self.items[item]
    
    @property
    def calculate_total(self):
        return sum(item.price*quantity for item,quantity in self.items.items())
    
    def clear_cart(self):
        self.items={}
        print("Cart cleared successfully!")
        
   

class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age=age
        self.designation=designation
        self.salary=salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        
    def add_employee(self,restaurant,employee):
        restaurant.add_employee(employee)
    
    def view_employee(self,restaurant):
        restaurant.view_employee()
    
    def add_menu_item(self,restaurant,item):
        restaurant.menu.add_menu_item(item)
        
    def remove_item(self,restaurant,item_name):
        restaurant.menu.remove_item(item_name)

class Restaurant:
    def __init__(self,name):
        self.name=name
        self.employees=[]
        self.menu=Menu()
    
    def add_employee(self,employee):
        self.employees.append(employee)
    
    def view_employee(self):
        print('Employee List')
        for emp in self.employees:
            print(emp.name,emp.phone,emp.email,emp.address)

class Menu:
    def __init__(self):
        self.items=[]
    
    def add_menu_item(self,item):
        self.items.append(item)
        
    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self,item_name):
        item=self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item deleted successfully!")
        else:
            print("Item not found!")
            
    def show_menu(self):
        print("********Menu********")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

class MenuItem:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity      

#create restaurant
mamar_bari=Restaurant("Mamar Bari")


# Create menu items
mn=Menu()
item=MenuItem("Burger",100,10)
item2=MenuItem("Pizza",200,20)

# Add menu items to the restaurant
admin=Admin("Admin User", "0987654321", "admin@example.com", "456 Side St")
admin.add_menu_item(mamar_bari,item)
admin.add_menu_item(mamar_bari,item2)


# Customer
customer1=Customer("John Doe", "1234567890", "john@example.com", "123 Main St")
customer1.view_menu(mamar_bari)

# Add item to cart
item_name=input("Enter item name to add to cart: ")
quantity=int(input("Enter quantity: "))
customer1.add_to_cart(mamar_bari,item_name,quantity)

customer1.view_cart()