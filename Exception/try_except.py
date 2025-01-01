"""
try_except -> statement
There are mainly two kinds of errors: syntax errors and exceptions

the code that may throw an exception will be written inside the try block
and if the exception inside the try block occurs then it will be handled by the except block\
"""

# print("Before Exception")

# a = int(input("Enter int: "))
# print(a)

# print("After Exception")

# Example - sales growth
# print("Enter the net sales for")

# previous = float(input("- Prior Period: "))
# current = float(input("- Current Period: "))

# change = (current - previous) * 100 / previous

# if change > 0:
#     result = f"Sales increased {abs(change)}%"
# else:
#     result = f"Sales decreased {abs(change)}%"

# print(result)
##################################################################
# Handling exception
# try:
#     print("Enter the net sales for")

#     previous = float(input("- Prior Period: "))
#     current = float(input("- Current Period: "))

#     change = (current - previous) * 100 / previous

#     if change > 0:
#         result = f"Sales increased {abs(change)}%"
#     else:
#         result = f"Sales decreased {abs(change)}%"

#     print(result)
# except:
#     print("Error! Please enter a number for net sales.")
###################################################################
# Catching specific exception

try:
    print("Enter the net sales for")

    previous = float(input("- Prior Period: "))
    current = float(input("- Current Period: "))

    change = (current - previous) * 100 / previous

    if change > 0:
        result = f"Sales increased {abs(change)}%"
    else:
        result = f"Sales decreased {abs(change)}%"

    print(result)

# Catching specific exception
# except ValueError as e:
#     # print(f"Error -> {e}")
#     print(f"Error! Please enter a number for net sales.")

# except ZeroDivisionError as e:
#     print(f"Error -> {e}")

# Catching multiple exceptions
# except (ValueError, ZeroDivisionError) as e:
#     print(f"Error -> {e}")

except Exception as e:
    print(f"Error -> {e}")