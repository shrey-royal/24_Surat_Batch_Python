"""
Set - A set is an unordered collection of items, every element should be unique (no duplicates allowed) and mutable means we can change the data inside any set.

set is mutable (changeable), unordered(no index), no duplicates allowed.

syntax:
mySet = {1, 2, 3, ..., n}
mySet = set()   # use this when you want to make an empty set
"""

# mySet = {1, 2, 23, 12, 3334, 354, 34, 23, 12, 5, 32}
# print(mySet, type(mySet))

# basics of set
# mySet = {1, 2, 3, "Python", 2.3, 'd'}
# print(mySet)

# mySet = {11, 23, 11, 34, 22, 34, 22, 45, 456, 546, 56, 45, 56}
# print(mySet)

# myList = ['veggies', 'snacks', 'biscoots', 'fruits', 'ice-creams', 'biscoots',  'chocolates']
# print(set(myList))

# Methods

# skills = {'Eating', 'Python Programming', 'Databases', 'Software design', 'Networking'}
# skills.add('Critical Thinking')
# print(skills)
# skills.discard('Python Programming')
# print(skills)

mySet = {23, 45, 79, 34, 13}
dummy_set = {23, 45, 799, 34, 13}
disjoint_set = {2, 3}
new_set = {23, 45}

# print(mySet.difference(dummy_set))
# print(dummy_set.difference(mySet))
# mySet.difference_update(dummy_set)

# print({1, 2, 3}.isdisjoint({23, 22, 4}))
# print(mySet.intersection(dummy_set))
# mySet.intersection_update(dummy_set)
# print(new_set.issubset(dummy_set))
# print(mySet.pop())
# mySet.remove(23)
# print(mySet.symmetric_difference(dummy_set))
# mySet.symmetric_difference_update(dummy_set)
# mySet.update((122, 3243))
# print({1, 2, 3}.union({4, 5, 6}))
# del mySet, dummy_set
print(mySet, dummy_set, sep="\n")