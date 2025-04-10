# Wrapper function
def wrapper_function(func):  # Decorator function
    def inner():
        print("Before function runs")
        func()
        print("After function runs")
    return inner

# Original function
def say_hello():
    print("Hello World!")

# Wrap the original function
wrapped_hello = wrapper_function(say_hello)

wrapped_hello()
