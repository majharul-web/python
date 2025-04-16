from ride import RideSharing
from users import Rider, Driver
# -------------------- Demo Execution --------------------

niye_jao = RideSharing("Niye Jao")

# Add rider
rahim = Rider(name="Rahim", email="rahim@example.com", nid=123456789, current_location="Mohakhali", initial_amount=1000)
niye_jao.add_rider(rahim)

# Add driver
karim = Driver(name="Karim", email="karim@example.com", nid=987654321, current_location="Mohakhali")
niye_jao.add_driver(karim)

# Rider requests a ride
rahim.request_ride(niye_jao, destination="Dhanmondi", vehicle_type="car")

# Show ride info
rahim.show_current_ride()

# Driver ends the ride
karim.reach_destination(rahim.current_ride)

# Company summary
print(niye_jao)
