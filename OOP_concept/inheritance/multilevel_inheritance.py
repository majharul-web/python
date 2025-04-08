class Vehicle:
    def __init__(self,color,brand):
        self.color=color
        self.brand=brand
    
    def __repr__(self,type):
        return f'This is a {self.brand} {self.color} color {type} '

class Truk(Vehicle):
    def __init__(self, color, brand,capacity):
        super().__init__(color, brand)
        self.capacity=capacity

class Pickup(Truk):
    def __init__(self, color, brand, capacity,owner):
        super().__init__(color, brand, capacity)
        self.owner=owner
    def __repr__(self, type):
        return f'This is a {self.brand} {self.color} color {type},Capacity:{self.capacity} and Owner:{self.owner}'
       

vehicle=Pickup("blue","toyota","550 kg","MIJ").__repr__("buss")
print(vehicle)