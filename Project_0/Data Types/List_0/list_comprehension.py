"""
List Comprehension: [expression for item in iterable if condition]

for else -> [expression_1 if condition else expression_2 for item in iterable]

"""

# l = [i for i in range(10)]
# l = [i**2 for i in range(1, 11)]
# l = [i**2 for i in range(1, 11) if i%2 == 0]
# l = [i**2 if i%2 == 0 else i for i in range(1, 11)]
l = [int(i**0.5) for i in [i**2 for i in range(1, 11) if i%2 == 0]]

print(l)