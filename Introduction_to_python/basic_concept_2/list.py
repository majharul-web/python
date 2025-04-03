# list, array, collection is same
from operator import index

# index =  0  1  2  3  4  5  6  7  8
numbers = [45,56,12,89,87,32,84,59,93]
# index = -9 -8  -7 -6 -5 -4 -3 -2 -1

# print(numbers[3],numbers[-1])



'''

print(numbers[2:6])
print(numbers[1:7:1])
print(numbers[1:7:2])
print(numbers[1:7:-1])
print(numbers[7:1:-1])
print(numbers[7:1:-2])
print(numbers[4:])
print(numbers[:4])
print(numbers[:])
print(numbers[::-1])

'''
numbers.append(45)
last=numbers.pop()
numbers.insert(1,20)
numbers.remove(84)

print(numbers,last)

index_at=numbers.index(56)
print(index_at)

print(numbers.reverse())

numbers_with_index=enumerate(numbers)
for index,val in numbers_with_index:
    print(f"{index}={val}")