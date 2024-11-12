# q1
# grades = [85, 90, 78, 92, 88]

# new_grade = 95
# grades.append(new_grade)

# remove_grade = 78
# if remove_grade in grades:
#     grades.remove(remove_grade)

# if grades:
#     avg_grade = sum(grades) / len(grades)
# else:
#     avg_grade = 0

# print("Update Grades:", grades)
# print("Average Grades:", avg_grade)

# q2
# employees = [("Alice", 30), ("Bob", 25), ("Charlie", 30), ("David", 22)]

# sorted_employees = sorted(employees, key=lambda emp: (emp[1], emp[0]))

# print("Sorted Employees:", sorted_employees)

# q3
# inventory = [("Apples", 10), ("Oranges", 5)]

# item_name = "Apples"
# quantity = 0

# item_found = False
# for i, (name, qty) in enumerate(inventory):
#     if name == item_name:
#         item_found = True
#         if quantity == 0:
#             inventory.pop(i)
#         else:
#             inventory[i] = (name, quantity)
#         break
# if not item_found and quantity != 0:
#     inventory.append((item_name, quantity))

# print("Updated Inventory:", inventory)

# q4
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# total = 0
# for i in range(len(matrix)):
#     total += matrix[i][i]

# print("Diagonal Sum:", total)

# q5
pair = (10, 20)
a, b = pair
swapped_pair = (b, a)
print("Swapped Pair:", swapped_pair)

pairs = [(1, 2), (3, 4), (5, 6)]
swapped_list = []
for pair in pairs:
    a, b = pair
    swapped_pair = (b, a)
    swapped_list.append(swapped_pair)

print("Swapped List:", swapped_list)
