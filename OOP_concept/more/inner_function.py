def outer_function(name):
    def inner_function():
        return f"Hello, {name}!"
    
    message = inner_function()  # Call inner function inside outer
    return message

print(outer_function("Majharul"))


def power_function(n):  # Outer
    def inner(x):       # Inner
        return x ** n
    
    return inner        # Return inner function


""" 
# Create a square function
square = power_function(2)

# Create a cube function
cube = power_function(3)

print(square(5))  
print(cube(2))   
"""  

print(power_function(2)(10))  # Output: 100
print(power_function(3)(3))   # Output: 27

