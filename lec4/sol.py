#1
# age = int(input("Enter age: "))
# nationality = input("Enter nationality: ").lower()

# if age >= 18 and nationality == "citizen":
#     print("Eligible to vote.")
# else:
#     print("Not Eligible to vote.")

#2
# sub1 = int(input("Enter marks in subject 1: "))
# sub2 = int(input("Enter marks in subject 2: "))
# sub3 = int(input("Enter marks in subject 3: "))

# if sub1 >= 50 and sub2 >= 50 and sub3 >= 50:
#     print("Passed...")
# else:
#     print("Failed...")

#3
# number = int(input("Enter a number: "))

# if 0 <= number <= 10:
#     print("Low range.")
# elif 11 <= number <= 20:
#     print("Medium range.")
# else:
#     if number % 2 == 0:
#         print("High range (even)")
#     else:
#         print("High range (odd)")

#4
# db_username = "user123"
# db_pass = "pass456"

# username = input("Enter username: ")
# password = input("Enter password: ")

# print("Login successful!" if username == db_username and password == db_pass else "Login failed.")

#5
number = int(input("Enter a number: "))

if 10 <= number <= 20:
    if number % 2 == 0:
        print("In range and even")
    else:
        print("In range and odd.")
else:
    print("Out of range.")