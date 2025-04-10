import math

# Decorator Function
def display_message(func):
    def wrapper(*args, **kwargs):  # Inner Wrapper Function
        print("Calculation Started...")
        result = func(*args, **kwargs)  # Call the actual function with all args and kwargs
        print("Calculation Ended...")
        return result
    return wrapper


# Applying the decorator on math.factorial using *args
@display_message
def factorial(n):
    return math.factorial(n)


# Call factorial with decorator
print("Factorial is:", factorial(5))  # Using positional argument


# Example with multiple arguments
@display_message
def add_numbers(a, b):
    return a + b


# Call add_numbers with *args
print("Sum is:", add_numbers(10, 15))  # Using multiple arguments


# Example with keyword arguments
@display_message
def greet(name, age=None):
    return f"Hello, {name}! You are {age} years old."

# Call greet with **kwargs
print(greet("Majharul", age=25))  # Using keyword arguments
