class Vehicle:
    def __init__(self, brand, color, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.brand = brand
        self.color = color

    def vehicle_info(self):
        return f'Brand: {self.brand}, Color: {self.color}'


class Technology:
    def __init__(self, gps, bluetooth, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gps = gps
        self.bluetooth = bluetooth

    def tech_info(self):
        return f'GPS: {self.gps}, Bluetooth: {self.bluetooth}'


class Car(Vehicle, Technology):
    def __init__(self, brand, color, gps, bluetooth, model):
        super().__init__(brand, color, gps, bluetooth)
        self.model = model

    def car_info(self):
        return f'{self.vehicle_info()}, Model: {self.model}, {self.tech_info()}'


car1 = Car("Toyota", "Red", "Available", "Available", "Corolla")

print(car1.car_info())
