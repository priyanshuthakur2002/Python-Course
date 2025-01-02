# Generators
import sys
# l = [x**2 for x in range(100000)]
# x = range(100000)

# print(f"Memory used by iterable: {sys.getsizeof(l)}")
# print(f"Memory used by iterator: {sys.getsizeof(x)}")

# def generate_numbers():
#     for i in range(5):
#         yield i

# gen = generate_numbers()

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

# print(next(gen))

# gen_exp = (x**2 for x in range(10000))
# l = [x**2 for x in range(10000)]
# print(next(gen_exp))
# print(next(gen_exp))

# print(sys.getsizeof(gen_exp))
# print(sys.getsizeof(l))

# def infite_numbers():
#     n = 0
#     while True:
#         yield n
#         n += 1

# gen = infite_numbers()
# for i in range(7):
#     print(next(gen))

def double_numbers(nums):
    for num in nums:
        yield num * 2

doubles = double_numbers(range(7))
# for num in doubles:
#     print(num)

# print(list(doubles))
list(doubles).append(14)

