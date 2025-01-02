# q1
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# multiply_by_2 = lambda x: x * 2

# num = int(input("Enter a number: "))
# result = multiply_by_2(factorial(num))
# print("Result:", result)

# q2
# def generate_fibonacci(n, fn):
#     def fibonacci(n):
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         else:
#             return fibonacci(n-1) + fibonacci(n-2)
        
#     result = []
#     for i in range(n):
#         result.append(fn(fibonacci(i)))
#     return result

# num = int(input("Enter a number: "))
# result = generate_fibonacci(num, lambda x: x * 2)
# print("Result:", result)

# q3
# def sum_of_digit(n):
#     if n == 0:
#         return 0
#     return n % 10 + sum_of_digit(n // 10)

# check_even_odd = lambda x: "Even" if x % 2 == 0 else "Odd"

# num = int(input("Enter a number: "))
# digit_sum = sum_of_digit(num)
# print(f"Sum of digits: {digit_sum}")
# print(f"The sum is {check_even_odd(digit_sum)}")

# q4
def create_power_function(exponent):
    def power(base):
        return base ** exponent
    return power

power_function = create_power_function(3)
print(power_function(2))
print(power_function(5))