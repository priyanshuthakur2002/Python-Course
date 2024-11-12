age = 20

if age >=18:
    print("Eligible")

else:
    print("Ineligible")




score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Work harder...")

print("Outside")

number = 15

# if number > 0:
#     if number % 2 == 0:
#         print("The number is positive and even.")
#     else:
#         print("The number is positive and odd.")
# else:
#     print("The number is not positive.")

# age = 20
# has_id = True

# if age >= 18 and has_id:
#     print("You may enter.")
# else:
#     print("Entry denied.")

# is_weekend = True
# is_holiday = False

# if is_weekend or is_holiday:
#     print("You can relax today!")
# else:
#     print("Time to work or study.")

# is_raining = False

# if not is_raining:
#     print("You can go for a walk.")
# else:
#     print("Better saty inside.")

# age = 16
# is_supervised = True

# if age >= 18 or (age >= 16 and is_supervised):
#     print("You can attend the event.")
# else:
#     print("You cannot attend the event.")

# age = 25
# if 18 <= age <= 30:
#     print("you are in the young adult age range")

age = 16
status = "Adult" if age >= 18 else "Minor"
print(status)
