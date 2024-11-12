# from decimal import Decimal
# Float
num1 = 5.0
num2 = -10.25

print(num1, num2)

# Dynamic Size

large_float = 3.4e38
small_float = 5.6e-05

print(large_float, small_float)

# Type Checking
num3 = 7.82
print(type(num3))

int_num = 10
float_num = float(int_num)

str_num2 = "10"
float_num2 = float(str_num2)

print(type(float_num), type(float_num2))

# Rounding Error
result = 0.1 + 0.2
print(round(result, 2))

# x = Decimal('0.1')
# y = Decimal('0.2')
# result = x + y
# print(result)


# Infinity
inf = float('inf')
neg_inf = float('-inf')
print(inf, neg_inf)

# NaN (Not a Number)
nan = float('nan')
print(nan == nan)