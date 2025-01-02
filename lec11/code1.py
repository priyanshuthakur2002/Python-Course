# Inheritance
# class ParentClass:
#     pass

# class ChildClass(ParentClass):
#     pass

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound."
    
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} barks."
    
# class Cat(Animal):
#     def __init__(self, name, can_speak):
#         super().__init__(name)
#         self.can_speak = can_speak
#     def purr(self):
#         return f"{self.name} is purring."
    
# animal = Animal("Generic Animal")
# dog = Dog("Buddy")
# cat = Cat("Whiskers", True)

# print(animal.speak())
# print(dog.speak())
# print(cat.speak())
# print(cat.purr())
# print(cat.can_speak)

# class Parent:
#     def __init__(self):
#         self.__private_attr = "I'm private!"

# class Child(Parent):
#     def access_private(self):
#         return self._Parent__private_attr
    
# child = Child()
# print(child.access_private())

# Encapsulation
#(Public, Protected, Private)
# Public members
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Hii, I'm {self.name}."
    

# person = Person("Alice", 20)
# print(person.name)
# print(person.greet())

# Protected members(_)
# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     def _greet(self):
#         return f"Hii, I'm {self._name}."
    
# class Employee(Person):
#     def display_greet(self):
#         return self._greet()
    
# employee = Employee("Bob", 25)
# print(employee.display_greet())

# print(employee._name)

# Private members(__)
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age

#     def greet(self):
#         return f"Hii, I'm {self.__name}."
    
#     @property
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, age):
#         self.__age = age
    
# person = Person("Alice", 25)
# print(person.greet())
# # print(person.__name)
# print(person.age)

# person.age += 1
# print(person.age)

# Polymorphism
# (Compile-Time, Run-Time)
# Method Overloading
# class Calculator:
#     def add(self, a, b=0, c=0):
#         return a + b + c
    
# calc = Calculator()
# print(calc.add(5))
# print(calc.add(5, 10))
# print(calc.add(5, 10, 15))

# Method Overriding
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound."
    
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} barks."
    
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} meows."
    
# animals = [Dog("Dog"), Cat("Cat"), Animal("Animal")]
# for animal in animals:
#     print(animal.speak())

# Operator Overloading
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
    
# p1 = Point(2, 3)
# p2 = Point(4, 5)
# p3 = p1 + p2
# print(f"({p3.x}, {p3.y})")

# Duck Typing
# class Dog:
#     def speak(self):
#         return "Dog barks"
    
# class Cat:
#     def speak(self):
#         return "Cat meows"
    
# class Robot:
#     def speak(self):
#         return "Robot beeps"
    
# def make_sound(entity):
#     print(entity.speak())

# make_sound(Dog())
# make_sound(Cat())
# make_sound(Robot())

# Polymorphism with Functions
# def add(a, b):
#     return a + b

# print(add(3, 4))
# print(add("Hello, ", "World!"))

# Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# shape = Shape()
rect = Rectangle(5, 10)
circle = Circle(7)

print(f"Rectangle's Area: {rect.area()}\nCircle's Area: {circle.area()}")
print(f"Rectangle's Perimeter: {rect.perimeter()}\nCircle's Perimeter: {circle.perimeter()}")