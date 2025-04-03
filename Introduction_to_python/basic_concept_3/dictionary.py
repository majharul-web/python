# Dictionary is a collection which is ordered** and changeable. No duplicate members.

person={"name":"sajid","age":21,"district":"dinajpur"}
print(person)
print(person.keys())
print(person.values())
print(person["name"])
person["job"]="empty"
del person['age']
print(person)

for key,value in person:
    print(f"{key}:{value}")