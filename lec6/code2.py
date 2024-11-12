# Adding elements
# items = [1, 2, 3]
# # items.append(4)
# # items.insert(len(items), 'a')
# items.extend([4, 5, 6])
# print(items)

# Removing elements
items2 = [1, 'a', 2, 3, 4, 5, 6, 'a']
# items2.remove('a')
# items2.pop(1)
# items2.clear()
count = items2.count('a')
for i in range(count):
    items2.remove('a')
print(items2)