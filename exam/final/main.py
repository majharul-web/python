# buss class
class Bus:
   def __init__(self, number, route, total_seats):
       self.number = number
       self.route = route
       self.total_seats = total_seats
       self.booked_seats = 0


   def available_seats(self):
       return self.total_seats - self.booked_seats


   def book_seat(self):
       if self.booked_seats < self.total_seats:
           self.booked_seats += 1
           return True
       return False


   def __repr__(self):
       return f"Bus Number: {self.number}, Route: {self.route}, Total Seats: {self.total_seats}, Available Seats: {self.available_seats()}"


# passenger class
class Passenger:
   def __init__(self, name, phone, bus):
       self.name = name
       self.phone = phone
       self.bus = bus


# admin class
class Admin:
   def __init__(self):
       self.username = "admin"
       self.password = "1234"


   def login(self, user, pw):
       return self.username == user and self.password == pw


# bus system class
class BusSystem:
   def __init__(self):
       self.buses = []
       self.passengers = []
       self.admin = Admin()
       self.is_logged_in = False


   def add_bus(self, number, route, total_seats):
       for bus in self.buses:
           if bus.number == number and bus.route.lower() == route.lower():
               print("Bus with this number already exists on the same route.")
               return
       bus = Bus(number, route, total_seats)
       self.buses.append(bus)
       print("Bus added successfully.")


   def find_bus(self, number):
       for bus in self.buses:
           if bus.number == number:
               return bus
       return None


   def book_ticket(self, number, name, phone):
       bus = self.find_bus(number)
       if bus:
           if bus.book_seat():
               passenger = Passenger(name, phone, bus)
               self.passengers.append(passenger)
               print("Ticket booked successfully.")
               print(f"Passenger Name: {name}, Phone: {phone}, Bus Number: {bus.number}, Route: {bus.route}")
               print(f"Fare: ৳500")
           else:
               print("No available seats on this bus.")
       else:
           print("Bus not found.")


   def show_buses(self):
       if not self.buses:
           print("No buses available.")
       else:
           for bus in self.buses:
               print(bus)


   def show_passengers_by_bus(self, number):
       print(f"Passengers for Bus {number}:")
       found = False
       for passenger in self.passengers:
           if passenger.bus.number == number:
               print(f"Name: {passenger.name}, Phone: {passenger.phone}")
               found = True
       if not found:
           print("No passengers found for this bus.")


   def search_buses_by_route(self, route):
       found = False
       for bus in self.buses:
           if bus.route.lower() == route.lower():
               print(bus)
               found = True
       if not found:
           print("No buses found on this route.")
          
   # admin menu
   def admin_menu(self):
       while True:
           print("Admin Menu:")
           print("1. Add Bus")
           print("2. View All Buses")
           print("3. View Passengers by Bus Number")
           print("4. Logout")
           action = input("Enter your action: ")
           if action == '1':
               number = input("Enter bus number: ")
               route = input("Enter route: ")
               try:
                   total_seats = int(input("Enter total seats: "))
                   self.add_bus(number, route, total_seats)
               except ValueError:
                   print("Invalid input. Total seats must be a number.")
           elif action == '2':
               self.show_buses()
           elif action == '3':
               number = input("Enter bus number to view passengers: ")
               self.show_passengers_by_bus(number)
           elif action == '4':
               self.is_logged_in = False
               print("Logged out successfully.")
               break
           else:
               print("Invalid action.")
              
   # any user menu
   def user_menu(self):
       while True:
           print("")
           print("Bangladesh Bus Ticket Booking System")
           print("1. Admin Login")
           print("2. Book Ticket")
           print("3. View All Buses")
           print("4. Search Bus by Route")
           print("5. Exit")
           action = input("Enter your action: ")
           if action == '1':
               username = input("Enter your username: ")
               password = input("Enter password: ")
               if self.admin.login(username, password):
                   print("Admin login successfully.")
                   self.is_logged_in = True
                   self.admin_menu()
               else:
                   print("Incorrect credentials! Please try again.")
           elif action == '2':
               number = input("Enter bus number to book: ")
               name = input("Enter your name: ")
               phone = input("Enter your phone: ")
               self.book_ticket(number, name, phone)
           elif action == '3':
               self.show_buses()
           elif action == '4':
               route = input("Enter route to search: ")
               self.search_buses_by_route(route)
           elif action == '5':
               print("Thank you for using our System. Goodbye!")
               break
           else:
               print("Invalid action. Try again.")






# Run the bus system
bd_bus_system = BusSystem()
bd_bus_system.user_menu()


