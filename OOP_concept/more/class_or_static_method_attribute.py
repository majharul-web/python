class Inventory:
    # Static Attribute (common to all products)
    store_name = "Majharul Electronics"

    def __init__(self, product_name, price, quantity):
        self.product_name = product_name #Instance attribute
        self.price = price
        self.quantity = quantity

    def product_info(self):
        return f'Product: {self.product_name}, Price: {self.price}, Quantity: {self.quantity}'

    # Method to add stock
    def add_stock(self, amount):
        self.quantity += amount

    # Method to sell product
    def sell_product(self, amount):
        if amount <= self.quantity:
            self.quantity -= amount
            print(f'{amount} {self.product_name} Sold!')
        else:
            print('Not enough stock!')

    # Class Method → Change store name
    @classmethod
    def change_store_name(self, new_name):
        self.store_name = new_name

    # Static Method → Check if available
    @staticmethod
    def check_availability(quantity):
        return "Available" if quantity > 0 else "Out of Stock"


# Create Products
p1 = Inventory("Laptop", 80000, 10)
p2 = Inventory("Headphone", 3000, 5)

print(p1.product_info())
print(p2.product_info())

# Sell Product
p1.sell_product(3)
p2.sell_product(6)  # Not enough stock

# Add Stock
p2.add_stock(10)
print(p2.product_info())

# Static Method Usage
print(Inventory.check_availability(p1.quantity))

# Class Method Usage
print("Store Name:", Inventory.store_name)
Inventory.change_store_name("Imran Electronics")
print("Updated Store Name:", Inventory.store_name)


 

# Instance Method → Deals with object specific data → self
# Class Method → Deals with class level data → cls
# Static Method → Just utility/helper → No self or cls







