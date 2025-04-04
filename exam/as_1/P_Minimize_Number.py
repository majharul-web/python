import math

# Function to count the number of times a number can be divided by 2
def count_divisions_by_two(num):
    count = 0
    while num % 2 == 0:
        num /= 2
        count += 1
    return count

def min_division(A):
    # Initialize min_divisions to infinity
    min_divisions = math.inf  

    for num in A:
        div_count = count_divisions_by_two(num)
        min_divisions = min(min_divisions, div_count)  
    return min_divisions

# Get the input values
N = int(input()) 
A = [int(x) for x in input().split()]

# Print the result
print(min_division(A))


