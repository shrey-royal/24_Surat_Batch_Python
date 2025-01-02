"""
try:
    # code that may occur exception
except:
    # code that handle exception
finally:
    # code that clean up (it will be executed no matter the exception occurs or not)
"""

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))

    print(a/b)

except (ValueError, ZeroDivisionError) as error:
    print(f"Error! -> {error}")

finally:
    print("Finishing up!")