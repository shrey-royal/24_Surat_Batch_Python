# Anonymous Functions in Python

# lambda parameters: expression => syntax

# variable = lambda parameter: expression   => function definition
# variable(parameter) => function calling

# Normal function
# def square(x):
#     return x*x

# ans = square(4)
# print(ans)

# lambda function
# square2 = lambda x: x*x
# print(square2(6))


# lambda with multiple parameters
# add = lambda a=23, b=34: a+b
# print(add(2, 3))
# print(add())


# parameterless lambda functions

# greet = lambda : "Hello!"
# print(greet())

# inline lambda
# print((lambda x : x*x*x)(3))
# -------------------------------------------------------------------------------

# map -> takes a function and applies it to transform the data
# pairs = [(2, 3), (4, 5), (6, 7)]

# def map_func(elem):
#     return elem[0] * elem[1]

# mappedList = list(map(map_func, pairs))
# mappedList = list(map(lambda elem: elem[0] * elem[1], pairs))
# print(mappedList)
# -------------------------------------------------------------------------------

# count the number of vowels in a list using map.
# names = ["Aarav", "Ishita", "Omkar", "Ananya", "Vivek", "Priya", "Deepak", "Kavya", "Rohit", "Meera"]

# def count_vowel(name):
#     vowels = "aeiouAEIOU"
#     return sum(1 for char in name if char in vowels)

# vowel_counts = list(map(count_vowel, names))
# for name, count in zip(names, vowel_counts):
#     print(f"{name}: {count} vowels")
# -------------------------------------------------------------------------------

# filter -> filters the data
# data = [1, 34, 23, 45, 56, 56, 34, 234, 23, 34, 45, 567, 678, 78, 67, 34, 23, 34, 56, 67,34, 34, 23, 23, 34, 234]

# def filter_func(elem):
#     return elem > 70

# filteredList = list(filter(filter_func, data))
# filteredList = list(filter(lambda elem: elem > 70, data))
# print(filteredList)
# -------------------------------------------------------------------------------

# sorted -> sorts the data
# fruits = [(2, '🍒'), (1, '🍉'), (4, '🍅'), (3, '🍎')]

# sortedFruits = sorted(fruits, key=lambda x: x[0]) # asc
# sortedFruits = sorted(fruits, key=lambda x: -x[0])  # desc
# print(sortedFruits)
# -------------------------------------------------------------------------------


# reduce -> goes from left to right and applies the functions.
from functools import reduce

# def mmax(a, b):
#     return a if a > b else b

# gemstones = [211, 4, 6, 8, 10, 11]
# biggest = reduce(mmax, gemstones)
# print(biggest)

# result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
# print(result)
# -------------------------------------------------------------------------------

multiple_of_6 = list(not (i % 6) for i in range(1, 10))
print(any(multiple_of_6)) # or
print(all(multiple_of_6)) # and