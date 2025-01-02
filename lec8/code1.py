# scope
# local scope
# def my_func():
#     local_variable = 10

#     print(local_variable)

# my_func()

# Enclosing scope
# def outer_function():
#     outer_variable = "I am outer"

#     def inner_function():
#         nonlocal outer_variable
#         outer_variable = "I am modified"
#         print(outer_variable)

#     inner_function()
#     print(outer_variable)

# outer_function()

# Global scope
# global_variable = "I am global"

# def my_function():
#     global global_variable
#     global_variable = "I am local"
#     print(global_variable)

# my_function()
# print(global_variable)

# Built-in scope (len, min, max)

# print(len("hello"))

# lambda function

# lambda arguments: expression

# add_ten = lambda x: x + 10
# def add_ten(x):
#     return x + 10
# print(add_ten(5))

# multiply = lambda x, y: x * y
# print(multiply(3, 4))

# numbers = [1, 2, 3, 4]
# # sequared_numbers = list(map(lambda x: x**2, numbers))
# def find_square(x):
#     return x ** 2
# sequared_numbers = list(map(find_square, numbers))
# print(sequared_numbers)

# multiply_add = lambda x: (lambda y: (lambda z: x * y + z))
# result = multiply_add(2)(3)(4)
# print(result)

def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(5, 3, lambda a, b: a + b)
result2 = apply_operation(5, 3, lambda a, b: a * b)
print(result)
print(result2)