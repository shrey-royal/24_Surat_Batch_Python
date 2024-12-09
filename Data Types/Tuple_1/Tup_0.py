"""
Tuple -> Immutable Sequence

syntax:
    tuple() -> represented by ()

Changeable? False
Duplicate Allowed? -> True

"""

# myTuple = tuple()
# print(myTuple, type(myTuple))

# myTuple = (3, 5, 2, 56, 8, 4, 3, 12, 5, 78, "2", ["2", 34, 2, 2])
# print(myTuple, type(myTuple))

# print("Index: ", myTuple.index(8, 2, 5))
# print("Len: ", len(myTuple))
# print("Count: ", myTuple.count(2))
# print("Count: ", myTuple[11].count(2))

# myTuple[11][2] = 23
# print(myTuple)

"""
Q) Ordering tuple by list
Input:
tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)], sortList = ['l', 'a', 'k', 'e']

Output:
[('l', 5), ('a', 1), ('k', 2), ('e', 6)]
"""

tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)]
sortList = ['l', 'a', 'k', 'e']

output = [t for sl in sortList for t in tupList if t[0] == sl]  # 16 iters

# 5 iters
# for sl in sortList:
#     for t in tupList:
#         print(sl, t)
#         if t[0] == sl:
#             output.append(t)
#             tupList.remove(t)
#             break
print(output)

"""
Example 2:
Python program to convert decimal to binary (in bytes)
Input:
tuple1 = (1234, 331, 437, 59, 63)

Output:
(binary of 1, binary of 2, binary of 3, binary of 4, binary of 5)
"""