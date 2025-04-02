"""
Learn basic variable,
variable type and type casting
"""
# str
name="Md Majharul Islam"
institue='Dinajpur Polytechnic Institute'

# int
age=25

# bool
maried=True

# float
CGPA=4.00

print(name,age,maried,CGPA)

# Get the Type
print(type(name))
print(type(age))

# Case-Sensitive : A will not overwrite a
a = 4
A = "Sally"
print(A,a)

# Many Values to Multiple Variables : assign values to multiple variables in one line
boy,girl="sajid","mitu"
print(boy,girl)

# One Value to Multiple Variables: assign the same value to multiple variables in one line
x="boss","toss"
print(x)

# Unpack a Collection : Extract the values into variables. This is called unpacking.

fruits=["mango","apple"]
x,y=fruits
print(x,y)

print("Kodom ali"+" "+"Kacha badam")

text=f"{name} like {fruits}"
print(text)



