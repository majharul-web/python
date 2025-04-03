# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
myset_1=set([1,2,3,4,5])
myset_2={'apple','banana'}

myset_1.add(52)
print(myset_2,myset_1)
for item in myset_1:
    print(item)

myset_2.remove('banana')
for item in myset_2:
    print(item)

myset_3=myset_1.union(myset_2)
print(myset_3)