import csv

# with open("example.csv", "r") as file:
#     reader = csv.reader(file)
#     next(reader)
#     for row in reader:
#         print(row)

# with open("example.csv", "r") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         if int(row['Price']) >= 600:
#             print(row)

# data = [
#     ["Name", "Age", "City"],
#     ["Alice", 30, "New York"],
#     ["Bob", 25, "San Francisco"],
#     ["Charlie", 35, "Chicago"]
# ]

# with open("output.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(data)
# print("CSV file written successfully!")

new_data = [
    ["David", 25, "Seattle"],
    ["John", 35, "Chicago"]
]

with open("output.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(new_data)
print("New data appended successfully!")