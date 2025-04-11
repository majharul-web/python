# Parent Class 1
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def vehicle_info(self):
        return f'Brand: {self.brand}, Color: {self.color}'


# Parent Class 2
class Technology:
    def __init__(self, gps, bluetooth):
        self.gps = gps
        self.bluetooth = bluetooth

    def tech_info(self):
        return f'GPS: {self.gps}, Bluetooth: {self.bluetooth}'


# Child class with multiple inheritance

class Car(Vehicle,Technology):
    def __init__(self, brand, color,gps,bluetooth,model):
        Vehicle.__init__(self,brand,color)
        Technology.__init__(self,gps,bluetooth)
        self.model=model

    def car_info(self):
        return f'{self.vehicle_info()}, Model: {self.model}, {self.tech_info()}'

# Object
car1 = Car("Toyota", "Red", "Available", "Available", "Corolla")

print(car1.car_info())