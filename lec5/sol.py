# q1
# text = input("Enter a string: ")
# vowels = "aeiou"

# for char in text:
#     if char in vowels:
#         print(f"First vowel found: {char}")
#         break
# else:
#     print("No vowels found")

# q2
# num = int(input("Enter a number: "))
# even_count = 0
# odd_count = 0

# while num > 0:
#     digit = num % 10
#     num = num // 10

#     if digit == 0:
#         continue

#     if digit % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print(f"Even digits: {even_count}")
# print(f"Odd digits: {odd_count}")

# q3
# sum_positive = 0

# while True:
#     num = int(input("Enter a number: "))
#     if num < 0:
#         break
#     sum_positive += num
# print(f"Sun of positive numbers: {sum_positive}")

# q4
# num = int(input("Enter a number greater than 1: "))

# if num <= 1:
#     print("Please enter a number greater than 1")
# else:
#     for i in range(2, int(num ** 0.5)+1):
#         if num % i == 0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")

# q5
n = 5

for i in range(n):
    for j in range(i+1):
        print(i+1, end=" ")
    print()
