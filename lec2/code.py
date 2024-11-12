# variables
x = 5
# x = "Hello"
print(x)

# Dynamically Typed
# case sensitive
age = 90
Age = 21
print(Age)

# variable names

age = 25
Name = "John"
user_name = "Alice"
total_3 = 150

# 1st_user
# user-name

x = 10
x = "Hello"

# variables are Pointers

a = 10
b = a
a = 15
print(b, a)

# Assigning Values to Variables

a = 10
x, y, z = 1, 2, 3
a = b = c = 10

# Data Types of Variables

# Integer (int)

x, y, z = 10, -5, 0
print(x, y, z, sep="\n")

# characteristics of Integers

# Unlimited Precision
big_num = 124653453587566537865547645453764654355456764566465
print(big_num)

# Binary(0b, 0B), Octal(0o, 0O) and Hexadecimal(0x, 0X)

binary_num = 0b1010
octal_num = 0o12
hex_num = 0xA
dec_num = 10
print(binary_num, octal_num, hex_num, dec_num)

# Type Checking
num = 10
print(type(num))

str_num = "10"
con_num = int(str_num)
print(type(str_num), type(con_num))

# Immutable Nature
num1 = 10
num1 = 11