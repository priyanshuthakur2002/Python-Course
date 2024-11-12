people = {
    "person1": {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    },
    "person2": {
        "name": "Bob",
        "age": 25,
        "city": "Los Angeles"
    }
}

# print(people["person1"]["name"])

# people["person1"]['occupation'] = 'Engineer'
# print(people["person1"])

# del people["person2"]['age']
# print(people['person2'])

# person1= {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# for key in person1.keys():
#     print(key)

# for value in person1.values():
#     print(value)

# for key, value in person1.items():
#     print(f"{key}: {value}")

# for index, key in enumerate(person1):
#     print(f"{index}: {key}")

for person, details in people.items():
    print(f"{person}")
    for key, value in details.items():
        print(f"{key}: {value}")
