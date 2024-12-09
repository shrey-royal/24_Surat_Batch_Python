# Dictionary - Ordered, Mutable and Unique (no duplicates) collection of pairs containing key and values

# (Keys must be unique and value may contain duplicates)

# myDict = {
#     "key": "value",
# }

# myDict = {
#     "key": "value",
#     "key2": 22,
# }
# print(myDict, type(myDict))

employee_data = {
    "EMP001" : {
        "name": "Ramjibhai Bharwaad",
        "department": "Marketing",
        "salary": 75000
    },
    "EMP002" : {
        "name": "Sumita Sen",
        "department": "HR",
        "salary": 65000
    },
    "EMP003" : {
        "name": "Aishwarya Ahir",
        "department": "Finance",
        "salary": 80000
    },
}

# print(employee_data)
# print(employee_data["EMP003"])
# print(employee_data["EMP003"]["salary"])
# employee_data["EMP003"]["salary"] = 82000
# print(employee_data["EMP003"]["salary"])
# print(employee_data["EMP004"])  # KeyError

newEmp = {
    "name": "Madhu Gupta",
    "department": "HR",
    "salary": 50000,
    "contact": 1234567890,
}

employee_data["EMP004"] = newEmp    # Adding a new pair into the dictionary
print(employee_data["EMP004"]["contact"])


# text = "the quick brown fox jumps over the lazy dog the quick fox"
# word_count = {}
#
# for word in text.split():
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
#
# print(word_count)