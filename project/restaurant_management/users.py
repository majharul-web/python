from abc import ABC, abstractmethod
from orders import Order


class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address
        
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
        
    def view_menu(self,restaurant):
        restaurant.menu.show_menu()

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
    
    def pay_bill(self):
        total=self.cart.calculate_total
        print("Total Bill:", total)
        self.cart.clear_cart()
        print("Payment successful!")
        


    
       
   




