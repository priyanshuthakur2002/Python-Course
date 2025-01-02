# file = open("test.txt", "r")
# print("File Name:", file.name)
# print("Mode:", file.mode)
# file.close()

# with open('test.txt', 'r') as file:
#     content = file.read(5)
#     file.seek(10)
#     print(file.tell())

# with open('test.txt', 'r') as file:
#     # file.seek(5)
#     # first_line = file.readline()
#     # # print(first_line, end="")
#     # print(first_line.strip())

#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line.strip())

# with open("test.txt", "r") as file:
#     lines = file.readlines()
#     for line in reversed(lines):
#         print(line.strip())

with open('test.txt', 'r') as file:
    for line in file:
        print(line.strip())