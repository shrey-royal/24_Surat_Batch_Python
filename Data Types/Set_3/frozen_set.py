# frozen set - immutable and constants
# when a frozen set is declared then it can't be changed

# set1 = frozenset({1, 23, 56, 78, 34, 89, 234})
# print(set1)
# print(type(set1))

fs = frozenset([1, 2, 3, 4, 5])

fs_union = fs.union([4, 5, 6, 7])
fs_intersection = fs.intersection([2, 3, 4, 5])

print(fs_union)
print(fs_intersection)

"""
# Summary of Collections

--> List - Ordered, Mutable & Allow Duplicates

--> Tuple = Ordered, Immutable & Allow Duplicates

--> Set - UnOrdered, Immutable & Unique (Duplicates Not Allowed)
    -> Frozen Set => UnOrdered, Immutable, Constant, Unique

--> Dictionary - ordered, Mutable & Unique(Keys), Duplicate Values are Allowed

"""