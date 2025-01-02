import datetime
# with open("example.txt", "w") as file:
#     file.write("This is the first line.\n")
#     file.write("This is the second line.\n")

# lines = ("First line.\n", "Second line.\n", "Third line.\n", "Fourth line.\n")

# with open("writeline_example.txt", "w") as file:
#     file.writelines(lines)

# user_input = input("Enter text to save to the file:")
# with open("example.txt", "w") as file:
#     file.write(user_input + "\n")

# user_input = input("Enter text to save to the file:")
# with open("example.txt", "a") as file:
#     file.write(user_input + "\n")

# with open("log_file.txt", "a") as file:
#     log_msg = f"{datetime.datetime.now()}: This is a log entry.\n"
#     file.write(log_msg)

# with open("log_file.txt", "r") as file:
#     content = file.read()
#     print(content)

# print("Log entry added...")

# with open("log_file.txt", "a+") as file:
#     log_msg = f"{datetime.datetime.now()}: This is a log entry.\n"
#     file.write(log_msg)

#     file.seek(0)

#     content = file.read()
#     print(content)

with open("log_file.txt", "r") as src, open("copy.txt", "w") as dest:
    dest.write(src.read())

print("File copied successfully...")