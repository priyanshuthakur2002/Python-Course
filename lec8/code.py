# def greet():
#     print("Hello, World!")
# greet()

# def cal_area(radius):
#     return 3.14 * radius ** 2

# def cal_circumference(radius):
#     return 2 * 3.14 * radius

# r = 5
# print("Area:", cal_area(r))
# print("Circumference:", cal_circumference(r))

# def greet(name):
#     print(f"Hello, {name}!")

# greet("Alice")
# greet("Bob")

# def subtract(a, b=3):
#     return a - b

# result = subtract(a=10)
# print(result)

# def sum_all(*a):
#     total = sum(a)
#     return total

# print(sum_all(1, 2, 3))
# print(sum_all(4, 5, 6, 7, 8))

# def display_info(**info):
#     info["salary"] = 90000
#     for key, value in info.items():
#         print(f"{key}: {value}")

# display_info(name="Alice", age=25, city="New York")

# return
# def add(a, b):
#     result = a + b
#     return result

# sum_value = add(5, 3)
# print(sum_value)

# def calculate_stats(numbers):
#     total = sum(numbers)
#     count = len(numbers)
#     average = total / count
#     return total, count, average

# numbers = [10, 20, 30, 40]
# a, b, c = calculate_stats(numbers)

# print(f"Total: {a}, Count: {b}, Average: {c}")

# def create_profile(name, age, city):
#     return {"name": name, "age": age, "city": city}

# profile = create_profile("Alice", 30, "New York")
# print(profile)

def check_even(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

print(check_even(4))
print(check_even(7))