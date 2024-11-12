# break
# text = "hello"
# for char in text:
#     if char == 'l':
#         print("Found 'l'")
#         break
#     print("Checking:", char)

# count = 1
# while count <= 5:
#     print("Count:", count)
#     if count == 3:
#         print("Stopping the loop as count reached 3")
#         break
#     count += 1

# continue
# text = "python"
# for char in text:
#     if char in "aeiou":
#         continue
#     print(char)

# num = 1
# while num <= 10:
#     if num % 2 != 0:
#         num += 1
#         continue
#     print(num)
#     num += 1

# else

# text = input("Enter any word: ")
# for char in text:
#     if char == 'z':
#         print("Found 'z'")
#         break
# else:
#     print("'z' was not found in the text")

# num = 8
# while num % 7 != 0:
#     if num > 12:
#         print("Number is too large...")
#         break
#     num += 1
# else:
#     print("Number stayed within the range...")

# Nested loops

# for i in range(3):
#     for j in range(2):
#         print(f"i = {i}, j = {j}")

# n = 5
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end="")
#     print()

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(f"i = {i}, j = {j}")
    print("End of inner loop...")

