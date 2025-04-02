numbers = [45,56,12,89,87,32,84,59,93]
odds=[]
for n in numbers:
    if n%5==0:
        odds.append(n)
print(odds)
odd_nums=[n for n in numbers if n%5==0]
print(odd_nums)