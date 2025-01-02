import math
import random

# print("Pi:", math.pi)
# print("Euler's Number:", math.e)

# Rounding Functions
# math.ceil, math.floor, math.trunc
# print(math.ceil(4.7), math.floor(4.7), math.trunc(4.7))

# Power and Logarithm
# math.paw(x, y), math.sqrt(x), math.log(x, base), math.exp(x)
# print("2^3:", math.pow(2, 3))
# print("Square root of 16:", math.sqrt(16))
# print("Log base 2 of 8:", math.log(8, 2))
# print("e^2:", math.exp(2))

# Trigonometric Functions
# angle = 90
# radians = math.radians(angle)
# print("Sine of 90 degrees:", math.sin(radians))
# print("Cosine of 90 degrees:", math.cos(radians))

# Advanced Functions
# math.factorial(x), math.gcd(x, y)
# print("Factorial of 5:", math.factorial(5))
# print("GCD of 28 and 35:", math.gcd(28, 35))

# random module
# print("Random float between 0 and 1:", random.random())
# print("Random float between 10 and 20:", random.uniform(10, 20))

# print("Random interger between 1 and 10:", random.randint(1, 10))
# items = ['apple', 'banana', 'cherry']
# print("Random choice:", random.choice(items))
# random.shuffle(items)
# print("Shuffled list:", items)

random.seed(42)
print("Random number with seed 42:", random.randint(1, 10))