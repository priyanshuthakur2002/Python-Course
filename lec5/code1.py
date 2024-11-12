# count = 5
# while count > 0:
#     print(count)
#     count -= 1
# print(count)

# text = "Python"
# reversed_text = ""
# index = len(text) - 1
# while index >= 0:
#     reversed_text += text[index]
#     index -= 1
# print("Reversed String: ", reversed_text)

# text = "banana"
# index = 0
# count = 0
# while index < len(text):
#     if text[index] == 'a':
#         count += 1
#     index += 1
# print("Number of 'a' characters: ", count)

# password = "12345"
# print("Enter your password: ")
# entered_pass = input()
# while password != entered_pass:
#     entered_pass = input("Password is wrong!\n")
# print("Password accepted...")

text = "Hello World"
count = 0
while count < len(text) and text[count] != ' ':
    count += 1
print("Chracters before first space: ", count)