# Base Class
class Vehicle:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand
    
    def details(self):
        return f"This is a {self.color} {self.brand} vehicle."


# Intermediate Class
class Truck(Vehicle):
    def __init__(self, color, brand, capacity):
        super().__init__(color, brand)
        self.capacity = capacity

    def details(self):
        return f"{super().details()} It has a capacity of {self.capacity}."


# Derived Class
class Pickup(Truck):
    def __init__(self, color, brand, capacity, owner):
        super().__init__(color, brand, capacity)
        self.owner = owner

    def details(self):
        return f"{super().details()} Owner: {self.owner}"


# Object Creation
pickup = Pickup("Blue", "Toyota", "550 kg", "MIJ")

print(pickup.details())
