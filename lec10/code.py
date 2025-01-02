# Comprehensions

# list comprehensions
# [expression for item in iterable if condition]

# numbers = [1, 2, 3, 4, 5]
# # squares = [x**2 for x in numbers]
# # print(squares)
# even_numbers = [x for x in range(10) if x % 2 == 0]
# print(even_numbers)

# words = ["hello", "world", "python"]
# uppercased = [word.upper() for word in words]
# print(uppercased)

# pairs = [(x, y) for x in range(2) for y in range(3)]
# print(pairs)

# dictionary comprehensions
# {key_expression: value_expression for item in iterable if condition}

# square_dict = {x: x**2 for x in range(5)}
# filtered_dict = {x: x**2 for x in range(10) if x % 2 == 0}

# def categorize(num):
#     return "Even" if num % 2 == 0 else "Odd"
# categorized_dict = {x: categorize(x) for x in range(5)}
# print(categorized_dict)

# set comprehensions
# {expression for item in iterable if condition}

# numbers = [1, 2, 2, 3, 4, 4]
# unique_squares = {x**2 for x in numbers}
# print(unique_squares)

# unique_even_squares = {x**2 for x in range(10) if x % 2 == 0}
# print(unique_even_squares)

# numbers = [1, 2, 3, 4, 5]
# squares = []
# for x in numbers:
#     squares.append(x**2)

# print(squares)
# squares = [x**2 for x in numbers]
# print(squares)

# student_scores = {"Alice": 85, "Bob": 90, "Charlie": 78}
# passed_students = [name for name, score in student_scores.items() if score >= 80]
# print(passed_students)

categorization = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(categorization)

