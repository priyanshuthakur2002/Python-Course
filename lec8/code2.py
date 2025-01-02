# Higher-order Function:
# Accept a function
# Return a function
# def apply_operation(x, y, operation):
#     return operation(x, y)

# def add(x, y):
#     return x+y

# def multiply(x, y):
#     return x*y

# result_add = apply_operation(5, 4, add)
# result_mutiply = apply_operation(5, 4, multiply)

# print("Addition:", result_add)
# print("Multiplication:", result_mutiply)

# def create_mutiplier(factor):
#     return lambda x: x * factor

# double = create_mutiplier(2)
# triple = create_mutiplier(3)

# print("Double 5:", double(5))
# print("Triple 5:", triple(5))

# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

# closures
# def outer_function(message):
#     a = 45
#     def inner_function():
#         print(message, a)
#     return inner_function

# closure = outer_function("Hello, world!")
# closure()

# Decorators
# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}...")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} finished executing.")
#         return result
#     return wrapper

# @log_decorator
# def greet(name):
#     print(f"Hello, {name}!")

# # greet = log_decorator(greet)
# greet("Alice")

# Recursive Function
# def recursive_function(a):
#     if a > 6:
#         a -= 1
#         recursive_function(a)
#         print(a)

# recursive_function(10)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))