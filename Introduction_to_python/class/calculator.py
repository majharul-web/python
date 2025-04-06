class Calculator:
    # Constructor (Optional here)
    def __init__(self):
        print("Calculator is Ready")

    # Addition
    def add(self, a, b):
        return a + b

    # Subtraction
    def subtract(self, a, b):
        return a - b

    # Multiplication
    def multiply(self, a, b):
        return a * b

    # Division
    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


# Create Object
calc = Calculator()

# Operations
print("Addition: ", calc.add(10, 5))
print("Subtraction: ", calc.subtract(10, 5))
print("Multiplication: ", calc.multiply(10, 5))
print("Division: ", calc.divide(10, 5))
print("Division by Zero: ", calc.divide(10, 0))
