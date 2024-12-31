"""
# unpacking

a = 1, 2 => (1, 2)

a, b = 2, 3 => a = 2, b = 3

a, b, c = (1, 2, 3)


# a, b, c, d, e = [1, 2, 3, 4, 22]
# a, b, c, d, e = "Royal"

# print(a, b, c, d, e, sep='\t')
"""
# *args

# *a, b, c = 1, 2, 3, 4, 22
# a, *b, c = 1, 2, 3, 4, 22
# a, *b = 1, 2, 3, 4, 22

# print(a + sum(b))

# def add(*nums):
#     return sum(nums)

# print(add(2, 3, 23, 23, 23, 34, 4, 34, 23, 23, 34, 34, 45, 34, 23, 34, 45, 45, 342, 2))
"""
##### make a function in python to check in which quadrant my line forms

# Example usage:
p1 = (2, 3)
p2 = (-1, -4)

result = find_quadrant(p1, p2)
print(result)
"""

# def add(x, y, *nums, z):
#     print(x + y + sum(nums) + z)

# add(1, 2, 3, 4, 5, 6, 7, 8, 9, z=10)


########################################################
# **kwargs -> keyword arguments

def connect(**connection_info):
    print(type(connection_info))
    print(connection_info)

# connect(server='localhost', port=8080, user='admin', password="root")

# config = {'server':'localhost', 'port':8080, 'user':'admin', 'password':'root'}
# connect(**config)

connect(connection_info=[1, 2, 3], name="Yugbhai")