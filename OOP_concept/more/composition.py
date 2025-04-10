# Component 1: CPU Class
class CPU:
    def __init__(self, brand, cores, clock_speed):
        self.brand = brand
        self.cores = cores
        self.clock_speed = clock_speed

    def get_info(self):
        return f"CPU: {self.brand}, Cores: {self.cores}, Clock Speed: {self.clock_speed} GHz"


# Component 2: RAM Class
class RAM:
    def __init__(self, size, speed):
        self.size = size
        self.speed = speed

    def get_info(self):
        return f"RAM: {self.size} GB, Speed: {self.speed} MHz"


# Component 3: Storage Class
class Storage:
    def __init__(self, type_, size):
        self.type_ = type_
        self.size = size

    def get_info(self):
        return f"Storage: {self.size} GB, Type: {self.type_}"


# Main Class: Computer Class that uses Composition
class Computer:
    def __init__(self, brand, cpu, ram, storage):
        self.brand = brand
        self.cpu = cpu      # Composition: Computer has a CPU
        self.ram = ram      # Composition: Computer has RAM
        self.storage = storage  # Composition: Computer has Storage

    def get_computer_info(self):
        # Combining information from CPU, RAM, and Storage to present the full computer specs
        return f"{self.brand} Computer\n{self.cpu.get_info()}\n{self.ram.get_info()}\n{self.storage.get_info()}"


# Creating Components (objects of CPU, RAM, and Storage)
cpu = CPU(brand="Intel", cores=8, clock_speed=3.5)
ram = RAM(size=16, speed=3200)
storage = Storage(type_="SSD", size=512)

# Creating a Computer object using Composition
my_computer = Computer(brand="Dell", cpu=cpu, ram=ram, storage=storage)

# Get and Print the full computer information
print(my_computer.get_computer_info())


""" 
Inheritance and Composition are two key concepts in object-oriented programming (OOP) that help in organizing code and defining relationships between classes. Here’s a comparison of both:

1. Inheritance
Inheritance is a mechanism where one class (called a subclass or child class) inherits the properties and behaviors (methods) of another class (called a superclass or parent class). It models a "is-a" relationship between the parent and child classes.

Key Points:
"is-a" Relationship: A subclass is a specialized version of a parent class.

Reusability: The subclass can reuse methods and properties of the parent class.

Extensibility: You can add more specific behavior in the child class that is not present in the parent.

Tight Coupling: Subclasses are tightly coupled with their parent classes. Changes in the parent class can affect the subclasses.



2. Composition
Composition is a design principle where one class is composed of other classes (objects) as attributes. It models a "has-a" relationship. Rather than inheriting from a class, you include instances of other classes inside a class to compose complex behavior.

Key Points:
"has-a" Relationship: A class has objects of other classes as attributes.

Flexibility: The objects can change dynamically and are independent of the composed class.

Loose Coupling: It creates a more flexible and loosely coupled system, as changes to the component classes do not necessarily affect the class that contains them.

Reusability: Components (like CPU, RAM, Storage) can be reused across different classes, not just one class.



"""