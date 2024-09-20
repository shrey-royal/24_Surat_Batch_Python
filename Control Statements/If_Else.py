"""
Conditional Statements:

1. Using branching
print()

if this than that

age > 18 : print("Adult")
age < 18 : print("kid")


-> if statement
-> switch case

2. Using looping:

-> for loop
-> while loop
-------------------------------------


if condition:
    //
else:
    //

4 types of if else statement
    -> if statement
        if condition:
            //statement

    -> if else statement
        if condition:
            //statement
        else:
            //statement
    
    -> ladder if statement
        if condition:
            //statement
        elif condition:
            //statement
        elif condition:
            //statement
        else:   # default
            //statement
    
    -> nested if
        if condition:
            # nested if statement
            if condition:
                //statement
            else:
                //statement
        else:
            //statement
    
python does not have switch case.
python have match case which is switch case only but with a different name
"""

age = int(input("Enter age: "))

# if age > 18:
#     print("You are Adult.")
# else:
#     print("You are Kid.")

if age > 0 and age < 18:
    print("You are KID")
elif age >= 18 and age < 60:
    print("You are ADULT")
elif age >= 60 and age < 100:
    print("You are Senior Citizen")
else:
    print("Invalid age!")