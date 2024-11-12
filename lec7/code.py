# my_set = {1, 2, 3, 4}
# print(my_set)

# set_b = set([1, 2, 3, 4])
# set_b = set((1, 2, 3, 4))
# print(set_b)

# empty_set = set()
# print(type(empty_set))

# valid_set = {1 + 5j, "hello", (3, 4)}
# print(valid_set)

# invalid_set = {1, [2, 3]}
# print(invalid_set)

# Adding Elements
# my_set = {1, 2, 3}
# # my_set.add(4)
# my_set.update({4, 5, 6, 3})
# print(my_set)

# Removing Elements

# my_set = {1, 2, 3}
# my_set.remove(2)
# my_set.discard(4)
# a = my_set.pop()
# print("Removed:", a)
# my_set.clear()
# del my_set
# print(my_set)

#union
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}

# # union_set = set_a.union(set_b)
# union_set = set_a | set_b
# print(union_set)

#intersection
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}

# # intersection_set = set_a.intersection(set_b)
# intersection_set = set_a & set_b
# print(intersection_set)

#difference
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}

# # difference_set = set_a - set_b
# difference_set = set_a.difference(set_b)
# difference_set2 = set_b.difference(set_a)
# print(difference_set)
# print(difference_set2)

# symmetric difference
# set_a = {1, 2, 3}
# set_b = {3, 4, 5}

# # symmetric_difference_set = set_a.symmetric_difference(set_b)
# symmetric_difference_set = set_a ^ set_b
# print(symmetric_difference_set)

# Subset
# set_a = {1, 2, 3}
# set_b = {1, 2, 3, 4, 5}

# # print(set_a <= set_b)
# print(set_a.issubset(set_b))

# Superset
# set_a = {1, 2, 3}
# set_b = {1, 2, 3, 4, 5}

# print(set_b >= set_a)
# print(set_b.issuperset(set_a))

# Proper subset or superset
# set_a = {1, 2, 3}
# set_b = {1, 2, 3, 4, 5}

# print(set_b > set_a)
# print(set_a < set_b)

# disjoint sets
# set_a = {1, 2, 3}
# set_b = { 4, 5}

# print(set_a.isdisjoint(set_b))

# my_set = {"apple", "orange", "cherry"}
# for item in my_set:
#     print(item)

# even_numbers = {2, 4, 6, 8}
# for number in even_numbers:
#     if number % 4 == 0:
#         print(f"{number} is divisible by 4.")

# Frozensets

frozen = frozenset([1, 2, 3, 4])
print(frozen)
# frozen.add(5)

frozen_a = frozenset([1, 2, 3])
frozen_b = frozenset([2, 3, 4])

print(frozen_a | frozen_b)
print(frozen_a & frozen_b)
print(frozen_a - frozen_b)

