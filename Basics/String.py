# String declaration

# name = "Jay Vaghasiya"
# message = "Hello, Vaghasiya"

# print(name)
# print(message)

# f_ormatted strings (fstring)

# message = f"Good Morning, {name}"
# print(message)

# greetings = 'Good' 'Morning!' 'Naimishji'   # concatenation
# print(greetings)

# greeting = 'Good '
# time = 'Evening'

# greeting = greeting + time + '!'
# print(greeting)

# -----------------------------------------------------------

# Accessing string element

# str = None

# str = 'Python String'
# print(str[0])
# print(str[12])

# print(len(str))

# print(str[-1])
# print(str[12])
# -----------------------------------------------------------

# Slicing - a TECHNIQUE that helps in extraction of specific words/parts from string.

# syntax: Sequence[start(inclusive):end(exclusive):step-1]

word = "Artificial_Intelligence"

# Positive Slicing

# print(word[4:10])
# print(word[4:10])
# print(word[:4])
# print(word[11:])

'''
# smol praktis
# new_word = word[:4] + '-' + word[4:10]
new_word = f'{word[:4]} - {word[4:10]}'
print(new_word)
'''

# Another example
# mithai = "Kesar Katri ane Malai Barfi"
# print()

# Step - skip characters

# word = "0_1_2_3_4_5_6_7_8_9"

# print(word[::3])    # step = 2 (working: step-1)
# print(word[::4])    # even
# print(word[2::4])    # odd

naam = "Naimishji"
# Niihi
# amsj
# Namihj
# aiisji
# isi