list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2
print(combined_tuple)

# repeated_list = list1 * 2
# print(repeated_list)
# print(tuple1 * 2)

# fruits = ["apple", "banana", "cherry"]
# print("apple" in fruits)
# print("mango" in fruits)

# colors = ("red", "green", "blue")
# print("green" in colors)
# print("yellow" not in colors)

print(len(list2))
print(len(tuple1))

print(max(list1), min(list1))
print(max(tuple1), min(tuple1))

# unpacking
coordinates = (10, 20, 30)
x, *y, z = coordinates
print(x, y)

numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(first, middle, last)

