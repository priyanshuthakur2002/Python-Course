# q1
# set_a = {1, 2, 3, 4}
# set_b = {2, 3, 5}
# set_c = {2, 3, 6}

# common_elements = set_a & set_b & set_c

# print(common_elements)

# q2
# words = ["apple", "banana", "apple", "orange", "banana", "apple"]

# word_counts = {}

# for word in words:
#     if word in word_counts:
#         word_counts[word] += 1
#     else:
#         word_counts[word] = 1

# print(word_counts)

# q3
# lst = [1, 2, 2, 3, 4, 4, 5]

# unique_elements = set(lst)
# count = len(unique_elements)

# print(count)

# q4
# lst_tuple = [(1, 2, 3),(4, 5, 6),(1, 2, 3)]

# frozenset_dict = {}

# for triplet in lst_tuple:
#     frozen_key = frozenset(triplet)
#     triplet_sum = sum(triplet)
#     frozenset_dict[frozen_key] = triplet_sum

# print(frozenset_dict)

# q5
set1 = {1, 2, 3}
set2 = {2, 3, 4}

sym_diff = set1 ^ set2

print(sym_diff)