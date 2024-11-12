fruits = ["apple", "banana", "cherry", "date", "fig"]
fruits_tuple = ("apple", "banana", "cherry")
# print(fruits[0])
# print(fruits_tuple[1])

# Slicing
# print(fruits[0:1])
# print(fruits_tuple[0:])
# print(fruits[::2])
# print(fruits[::])
# print(fruits[::-1])

# Negative Indexing
print(fruits[-1])
print(fruits_tuple[-2])

mixed_list = [42, "hello", 3.14, True, ("apple", 25, False)]
# print(mixed_list)
for i in mixed_list:
    print(i)

# 2D list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(matrix)

# for i in matrix:
#     for j in i:
#         print(j, end=" ")
#     print()

