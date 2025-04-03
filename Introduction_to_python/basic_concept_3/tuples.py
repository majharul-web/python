
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

mytuple_1=1,2,3
mytuple_2=(1,2,3,'tuple')
mytuple_3=tuple(('tx',True,1))
print(mytuple_3)
print(mytuple_3[0])
print(mytuple_1[-1])
print(mytuple_2[1:])

for item in mytuple_3:
    print(item)

i_1,*all=mytuple_2
print(i_1,all)

# mytuple_1[0]=5
