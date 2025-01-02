# q1
import csv

# data = [
#     ["Name","Roll No","Grade"],
# 	["John",101,"A"],
# 	["Alice",102,"B"],
# 	["Bob",103,"A"]
# ]

# with open("students.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

# with open("students.csv", 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# q2
# with open("students.csv", 'r') as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     top_students = [header]
#     for row in reader:
#         if row[2] == "A":
#             top_students.append(row)

# with open("top_students.csv", 'w', newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(top_students)

# print("Filtered students saved successfully!")

# q3
# with open("students.csv", 'r') as file:
#     reader = csv.reader(file)
#     header = next(reader)
#     row_count = 0
#     column_count = len(header)

#     for row in reader:
#         row_count += 1

# print(f"Number of rows: {row_count}\nNumber of columns: {column_count}")

# q4
updated_data = []
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    updated_data.append(header)

    for row in reader:
        row[1] = str(int(row[1]) + 100)
        updated_data.append(row)

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(updated_data)

print("Roll numbers updated successfully!")

