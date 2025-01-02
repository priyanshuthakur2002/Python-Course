# q1
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# employee = Employee("Alice", 60000)

# print(f"Employee Name: {employee.name}")
# print(f"Employee Salary: {employee.salary}")

# q2
# class BankAccount:
#     def __init__(self, account_number, owner, balance=0):
#         self.account_number = account_number
#         self.owner = owner
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Deposit amount must be positive!")
    
#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient balance...")

#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self, amount):
#         if amount >= 0:
#             self.__balance = amount
#         else:
#             print("Balance can't be negative!")

# account = BankAccount("12345", "Alice", 1000)

# print(f"Balance: {account.get_balance()}")

# account.deposit(500)
# print(f"Balance: {account.get_balance()}")

# account.withdraw(300)
# print(f"Balance: {account.get_balance()}")

# q3
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def display(self):
        return f"Width={self.width}, Height={self.height}, Area={self.area()}, Perimeter={self.perimeter()}"
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def display(self):
        return f"Radius={self.radius}, Area={self.area()}, Perimeter={self.perimeter()}"
    
rect = Rectangle(4, 5)
print(rect.display())

circle = Circle(7)
print(circle.display())