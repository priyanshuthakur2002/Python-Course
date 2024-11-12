# text = "Python"
# print(text[0])
# fourth_char = text[3]
# print(fourth_char)
# last_char = text[-1]
# print(last_char)
# second_last_char = text[-2]
# print(second_last_char)

# # IndexError [-len(str), len(str)-1]
# print(text[-len(text)])

# slicing [start:end:step] => [0:len(str):1]
text = "Hello, Python!"
substring = text[-6:-10:-1]
print(substring)
print(text[::])
print(text[::-1])
print(text[::2])
print(text[1::2])

print(text[len(text)+50:])