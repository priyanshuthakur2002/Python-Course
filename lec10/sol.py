# q1
# def transform_matrix(matrix):
#     return [
#         [x**2 if x % 2 == 0 else x*2 for x in row] for row in matrix
#     ]

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# result = transform_matrix(matrix)
# # print(result)
# for row in result:
#     print(row)

# q2
# def fibonacci_generator():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a+b

# fib_gen = fibonacci_generator()
# print([next(fib_gen) for x in range(10)])

# q3
# def flatten_list(nested_list):
#     return [item for sublist in nested_list for item in sublist]

# nested_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# result = flatten_list(nested_list)
# print(result)

# q4
import string

def word_lengths(sentence):
    return {
        word.strip(string.punctuation): len(word.strip(string.punctuation)) for word in sentence.split()
    }

sentence = "Hello, World! Practice makes perfect."

result = word_lengths(sentence)

print(result)