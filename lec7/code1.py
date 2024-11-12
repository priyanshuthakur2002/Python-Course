import copy
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# person = dict([("name", "Alice"), ("age", 30), ("city", "New York")])
# print(person)

# empty_dict = {}
# empty_dict2 = dict()

# print(empty_dict, empty_dict2)

# valid_dict = {
#     "name": "Alice",
#     1: "integer key",
#     (1, 2): "tuple key"
# }

# print(valid_dict)

# invalid_dict = {
#     ["name"]: "Alice"
# }

# print(invalid_dict)

# student = {
#     "name": "John",
#     "name": "Alice"
# }

# print(student)

# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# print(person["salary"])
# print(person.get("city", "Not specified"))

# Adding
# person["salary"] = 90000
# person["age"] = 31
# print(person)

# Removing

# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# del person["age"]
# del person["salary"]
# delete_value = person.pop("salary", "Not found")
# delete_value = person.popitem()
# print(delete_value)
# person.clear()
# print(person)

# common methods
# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York",
#     "letters": ['A', 'l', 'i', 'c', 'e']
# }
# keys_view = person.keys()
# print(keys_view)

# person['salary'] = 95000
# print(keys_view)

# print(person.values())
# print(person.items())

# copy_person = person.copy()
# person['letters'][0] = 'Z'
# person['age'] = 31
# print(copy_person)

# deep_copy = copy.deepcopy(person)
# person['letters'][0] = 'Z'
# print(deep_copy)
# print(person)

# person = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
# person.update({'salary': 90000, 'language': 'English'})
# print(person)

keys = ['name', 'age', 'city']
unknown_dict = dict.fromkeys(keys, "Unknown")
print(unknown_dict)