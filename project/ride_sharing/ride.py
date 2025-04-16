from datetime import datetime
from vehicle import  Car, Bike

# -------------------- Ride Classes --------------------

class Ride:
    def __init__(self, start_location, end_location, vehicle):
        self.vehicle = vehicle
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.distance = 10  # Example static distance
        self.estimated_fare = self.calculate_fare(self.distance)

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet += self.estimated_fare
        self.print_summary()

    def calculate_fare(self, distance):
        fare_per_km = {
            'car': 10,
            'bike': 5,
            'cng': 7
        }
        return distance * fare_per_km.get(self.vehicle.vehicle_type, 0)

    def print_summary(self):
        print("\n✅ Ride Completed! Summary:")
        print(f"🔸 From: {self.start_location}")
        print(f"🔸 To: {self.end_location}")
        print(f"🔸 Distance: {self.distance} km")
        print(f"🔸 Vehicle Type: {self.vehicle.vehicle_type.title()}")
        print(f"🔸 Rider: {self.rider.name}")
        print(f"🔸 Driver: {self.driver.name}")
        print(f"💰 Total Fare: {self.estimated_fare} BDT")
        print(f"👛 Rider Wallet Balance: {self.rider.wallet} BDT")
        print(f"👛 Driver Wallet Balance: {self.driver.wallet} BDT")
        print("-" * 45)

    def __repr__(self):
        return f"Ride from {self.start_location} to {self.end_location}, Driver: {self.driver.name}, Rider: {self.rider.name}"

class RideRequest:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.end_location = end_location

class RideMatching:
    def __init__(self, drivers):
        self.available_drivers = drivers

    def find_driver(self, ride_request, vehicle_type):
        if self.available_drivers:
            driver = self.available_drivers[0]
            if vehicle_type == 'car':
                vehicle = Car(vehicle_type, "ABC123", 100)
            elif vehicle_type == 'bike':
                vehicle = Bike(vehicle_type, "XYZ789", 50)
            else:
                print("Vehicle type not supported.")
                return None
            ride = Ride(ride_request.rider.current_location, ride_request.end_location, vehicle)
            driver.accept_ride(ride)
            return ride
        return None

# -------------------- RideSharing Company --------------------

class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.drivers = []
        self.riders = []
        self.rides = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_ride(self, ride):
        self.rides.append(ride)

    def __str__(self):
        return f"\n🚕 {self.company_name} has {len(self.drivers)} drivers and {len(self.riders)} riders"