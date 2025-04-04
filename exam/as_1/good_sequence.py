def good_sequence(n, arr):
    arr.sort()  # Step 1: Sort the array
    removals = 0
    i = 0

    while i < n:
        x = arr[i]  # Current number
        count = 0

        # Step 2: Count occurrences of x manually
        while i < n and arr[i] == x:
            count += 1
            i += 1  # Move to next element
        
        # Step 3: Determine the removals needed
        if count > x:
            removals += count - x  # Remove extra occurrences
        elif count < x:
            removals += count  # Remove all occurrences of x
    
    return removals

# Input
N = int(input())  # Read the first line as an integer
A = list(map(int, input().split()))  # Read space-separated integers into a list

# Output
print(good_sequence(N, A))



