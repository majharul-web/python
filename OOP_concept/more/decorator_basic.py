import math

# Decorator Function
def display_message(func):
    def wrapper(n):         # Inner Wrapper Function
        print("Calculation Started...")
        result = func(n)    # Call actual function
        print("Calculation Ended...")
        return result
    return wrapper


# Applying the decorator on math.factorial
@display_message
def factorial(n):
    return math.factorial(n)


# Call factorial with decorator
print("Factorial is:", factorial(5))
