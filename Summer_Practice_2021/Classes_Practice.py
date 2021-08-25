# Use classes to define new types
# How to define a new type and its methods
# First define a class, capitalize, no _
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# Object is an instance of a class
point1 = Point(100, 20)
point1.draw()

# Can also add attributes or edit attributes
point1.x = 10
point1.y = 20
print(point1.x)

# each object is a different instance
point2 = Point(5, 10)
point2.x = 20


# Constructor is a function that is called when object is created

# Create Person class with name attribute and talk method
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("John")
john.talk()
print(john.name)


# Inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass
