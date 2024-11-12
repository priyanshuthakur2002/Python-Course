# 1
num = 4563
first_digit = num // 1000
num = num % 1000
second_digit = num // 100
num = num % 100
third_digit = num // 10
num = num % 10
fourth_digit = num // 1

sum = first_digit + second_digit + third_digit + fourth_digit
print(sum)

# 2
num = 29
print(num % 2 == 0)

# 3

num = 9876
first_digit = num // 1000
num = num % 1000
second_digit = num // 100
num = num % 100
third_digit = num // 10
num = num % 10
fourth_digit = num // 1

print(fourth_digit, third_digit, second_digit, first_digit, sep="")

# 4

num = 25
binary = bin(num)
octal = oct(num)
hexadecimal = hex(num)

print(binary, octal, hexadecimal)

# 5

a = 5
b = 10
a, b = b, a
print(a, b)