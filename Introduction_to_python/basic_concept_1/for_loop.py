# basic for loop
from Introduction_to_python.basic_concept_1.variable import fruits

num=[1,2,3,4,5,6,7,8,9,10]
for n in num:
    print(n)

for f in fruits:
    print(f)

# loop in string
string="masud is very popular"

for s in string:
    if s=='s':
        continue
    print(s)

# range based for loop

for x in range(5):
    print(x)

for x in range(5,15,3):
    print(x)

