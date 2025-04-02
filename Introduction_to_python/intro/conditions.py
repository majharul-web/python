age=int(input("Enter your age : "))

if age>=18:
    print("You are adult")
elif age <18 and age>4:
    print("You are child")
else:
    print("You are infant")


# This technique is known as Ternary Operators, or Conditional Expressions.
a = 2
b = 330
print("A") if a > b else print("B")