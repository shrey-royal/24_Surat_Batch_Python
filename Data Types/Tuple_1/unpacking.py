# packing -> store multiple value in one variable

# n1, n2 = 1, 2
# print(n1, n2)

# n1 = 1, 2, 3, 4, 32, 1, 123, 12, 123, 2     # packing
# print(n1)

# unpacking
# n = (1, 2, 3, 4, 32, 1, 123, 12, 123, 2)
# n1, n2, n3 = n[0:3], n[3:-1], n[-1:]
# print(n1, n2, n3)

# * operator -> it takes multiple values
# n1, n2, *n3 = 1, 2, 3, 4, 2, 1, 1, 3, 2, 5, 2, 12, 4, 3
# n1, *n2, n3 = 1, 2, 3, 4, 2, 1, 1, 3, 2, 5, 2, 12, 4, 3
*n1, n2, n3 = 1, 2, 3, 4, 2, 1, 1, 3, 2, 5, 2, 12, 4, 3
print(n1, n2, n3)