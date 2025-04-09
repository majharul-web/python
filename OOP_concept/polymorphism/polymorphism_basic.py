# Parent Class
class Animal:
    def sound(self):
        return "Every animal makes a sound"


# Child Class
class Dog(Animal):
    def sound(self):
        return "Dog says: Woof Woof!"


# Child Class
class Cat(Animal):
    def sound(self):
        return "Cat says: Meow Meow!"


# Child Class
class Cow(Animal):
    def sound(self):
        return "Cow says: Moo Moo!"


# Polymorphism in action
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.sound())
