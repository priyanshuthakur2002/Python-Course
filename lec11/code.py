# classes and objects
# class Dog:
#     species = "Canis lupus familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# my_dog = Dog("Buddy", 3)
# my_dog2 = Dog("Max", 5)
# print(my_dog.name, my_dog.age)
# print(my_dog2.name, my_dog2.age)

# class ClassName:
#     def __init__(self, parameters):
#         # Initialization code

# (class -> PascalCase, attributes/methods -> snake_case)
# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age

# person1 = Person("Alice", 25)
# person2 = Person("Bob")

# print(person1.age)
# print(person2.age)

# Methods

# Instance methods

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Hi, I am {self.name} and I'm {self.age} years old."
    
# person = Person("Alice", 25)
# print(person.greet())

# class Person:
#     species = "Homo sapiens"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         return f"Hi, I am {self.name} and I'm {self.age} years old, and I belong to the species {Person.species}."
    
# person = Person("Alice", 25)
# print(person.greet())

# Class methods

# class Person:
#     population = 0

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Person.population += 1

#     @classmethod
#     def get_population(cls):
#         return f"Total population: {cls.population}"
    
# person1 = Person("Alice", 25)
# person2 = Person("Bob", 30)

# print(Person.get_population())

# Static methods

# class MathOperations:
#     @staticmethod
#     def add(a, b):
#         return a + b
    
#     @staticmethod
#     def multiply(a, b):
#         return a * b
    
# print(MathOperations.add(3, 5))
# print(MathOperations.multiply(3, 5))

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter    
    def name(self, name):
        self.__name = name

student = Student("Alice", 20)
student2 = Student('John', 25)
# print(student.__name)

student.name = "Bob"
print(student.name)
print(student2.name)