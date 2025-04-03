
def multiply(x, y):
    return x * y

print(multiply(2, 3))

# lambda function
lambda_multiply=lambda x,y:x*y
print(lambda_multiply(2, 3))

# map

double = lambda x: x * 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(double, numbers))
# Using lambda function with map
squared_numbers_2 = list(map(lambda x: x * x, numbers))
print(squared_numbers_2)

# filter
is_even = lambda x: x % 2 == 0
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(is_even, numbers))
# Using lambda function with filter
even_numbers_2 = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers_2)
print(even_numbers)

