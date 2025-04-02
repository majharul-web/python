name_1='Masud Rana\'s Khan'
name_2="Monir Khan"
name_3="""
hello monir khan
how are you
"""
print(name_1)
print(name_2)
print(name_3)

for char in name_2:
    print(char)
print(name_1[0])
print(name_1[:])
print(name_1[7:2:-1])

# name_2[0]='J'
print(name_1.upper())
print(name_1.lower())
print(name_1.capitalize())
print(name_1.swapcase())
print(name_1.title())
print(name_1.endswith('K'))
print(name_1.index('M'))

# String is immutable