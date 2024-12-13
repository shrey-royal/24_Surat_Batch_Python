"""
function: A named codeblock who performs operations and return the output(optional).

syntax:
def function_name(argument/s):
    body of the function
"""

def greet():
    print("Hello, there!")

# greet()

def add(x, y):
    # print(x+y)
    return x+y

# print(add(2, 33))

def palindrome(n):
    s = str(n)
    return s == s[::-1]
    

print(palindrome("aacdcaa"))
print(palindrome(12321))

# check armstrong number

# 15 - 26
# 153 - 1 + 125 + 27 = 153

def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    
    return total == number

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


# convert decimal to binary
# 8 -> 1000