class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary   # Protected Attribute

    # Getter Method
    @property
    def salary(self):
        return self._salary

    # Setter Method
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Invalid Salary! Salary can't be negative.")
        else:
            self._salary = value

    # Read-only Property
    @property
    def company(self):
        return "Tech IT Ltd"


# Create Object
emp1 = Employee("Majharul Islam", 50000)

# Access using Getter
print(emp1.name)
print(emp1.salary)     # internally -> emp1.salary() call

# Modify using Setter
emp1.salary = 60000    # internally -> emp1.salary(60000)
print(emp1.salary)

# Trying invalid Salary
emp1.salary = -1000    # won't update
print(emp1.salary)

# Read-only Property
print(emp1.company)    # Only Read, Can't Modify

# Trying to change Read-only Attribute
# emp1.company = "New Company"   # Error
