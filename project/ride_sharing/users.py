from abc import ABC, abstractmethod
from ride import RideRequest, RideMatching



class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        pass

class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_amount):
        super().__init__(name, email, nid)
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location

    def display_profile(self):
        print(f"Rider Name: {self.name}, Email: {self.email}, NID: {self.nid}")

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("Amount must be positive.")

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_request = RideRequest(self, destination)
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request, vehicle_type)
        if ride:
            ride.rider = self
            self.current_ride = ride
            ride_sharing.add_ride(ride)
            print(f"\n🚗 Ride requested from {self.current_location} to {destination} with vehicle type {vehicle_type.title()}")
        else:
            print("No drivers available at the moment.")

    def show_current_ride(self):
        if self.current_ride:
            print(self.current_ride)
        else:
            print("No current ride.")

class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location

    def display_profile(self):
        print(f"Driver Name: {self.name}, Email: {self.email}, NID: {self.nid}")

    def accept_ride(self, ride):
        ride.set_driver(self)
        ride.start_ride()

    def reach_destination(self, ride):
        ride.end_ride()


