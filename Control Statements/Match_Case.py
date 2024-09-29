"""
match case:

syntax:

match expression:
    case 1:
        //code
    case 2:
        //code
    case 3:
        //code
    case 4:
        //code
    .
    .
    .
    case n:
        //code

    case _:
        //default block
"""

print("".center(30, '-'))
print("Welcome to Naimishji's Hotel".center(30, ' '))
print("".center(30, '-'))

print()
print("📃 Naimishji's Menu: ")
print(" "*5, "1) Ganthiya (100 gm) > Rs.53")
print(" "*5, "2) Idli (3 pcs) > Rs.30")
print(" "*5, "3) Poha > Rs.20")
print(" "*5, "4) Dosa > Rs.70")
print(" "*5, "5) Khaman (100 gm) > Rs.35")
print(" "*5, "6) Locho (100 gm) > Rs.30")
print(" "*5, "7) Khavsa > Rs.30")
choice = int(input("Enter your choice: "))

match choice:
    case 1:
        qty = int(input("How many plates you want? > "))
        print(f"Total Price for {qty} plate/s Ganthiya is Rs.{53*qty}")
    case 2:
        qty = int(input("How many plates you want? > "))
        print(f"Total Price for {qty} plate/s Idli is Rs.{30*qty}")
    case 3:
        qty = int(input("How many plates you want? > "))
        print(f"Total Price for {qty} plate/s Poha is Rs.{20*qty}")
    case 4:
        qty = int(input("How many plates you want? > "))
        print(f"Total Price for {qty} plate/s Dosa is Rs.{70*qty}")
    case 5:
        qty = int(input("How many plates you want? > "))
        print(f"Total Price for {qty} plate/s Khaman is Rs.{35*qty}")
    case 6:
        qty = int(input("How many plates you want? > "))
        print(f"Total Price for {qty} plate/s Locho is Rs.{30*qty}")
    case 7:
        qty = int(input("How many plates you want? > "))
        print(f"Total Price for {qty} plate/s Khavsa is Rs.{30*qty}")
    case _:
        print("Invalid choice!")

print("Naimishji thanks you for your visit!")

"""
5 items each
1. BreakFast
2. Lunch
3. Snacks
4. Dinner
"""