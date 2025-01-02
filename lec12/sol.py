# q1
# from datetime import datetime

# dob_str = input("Enter your date of birth (YYYY-MM-DD)")
# dob = datetime.strptime(dob_str, "%Y-%m-%d")

# today = datetime.now()

# years = today.year - dob.year
# months = today.month - dob.month
# days = today.day - dob.day

# if days < 0:
#     months -= 1
#     days += (dob.replace(year= dob.year + (1 if dob.month == 12 else 0), month=(dob.month % 12) + 1) - dob.replace(day=1)).days

# if months < 0:
#     years -= 1
#     months += 12

# print(f"Age: {years} years, {months} months, and {days} days")

# q2
# import math
# import cmath

# def solve_quadratic(a, b, c):
#     if a == 0:
#         return "Not a quadratic equation."
    
#     discriminant = b**2 - 4*a*c

#     if discriminant > 0:
#         root1 = (-b + math.sqrt(discriminant)) / (2 * a)
#         root2 = (-b - math.sqrt(discriminant)) / (2 * a)
#         return f"Roots: x1 = {root1}, x2 = {root2}"
#     elif discriminant == 0:
#         root = -b / (2 * a)
#         return f"Root: x = {root}"
#     else:
#         root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
#         root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
#         return f"Complex Roots: x1 = {root1}, x2 = {root2}"
    
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))

# print(solve_quadratic(a, b, c))

# q3
from datetime import datetime

date1_str = input("Enter the first date (YYYY-MM-DD): ")
date2_str = input("Enter the second date (YYYY-MM-DD): ")

date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

delta = abs(date2 - date1)

print(f"Days Between: {delta.days} days.")