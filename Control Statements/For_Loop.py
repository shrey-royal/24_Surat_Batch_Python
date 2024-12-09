'''
Loop: Entry-Controlled Loop

1. for: fixed iteration
syntax:
    for iterator_var in iterable:
        # body

2. while: unfixed iteration
syntax:
    while condition:
        # body

'''

# range(start, stop, step) function

# for i in range(1, 10):
#     print(i, end=", ")

# user_input = int(input("Enter the end: "))

# for i in range(user_input):
#     print(i, end=", ")
# print("\b\b.")

# i = 1
# while i<=10:
#     print(i, end=", ")
#     i+=1

# -------------------------------------------------
# choice = 1
# while choice != 0:
#     print("1. Tea\n2. Coffee\n3. Milkshake\n4. Lassi\n0. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice > 0 and choice <= 4: print("Good!")
#     elif choice == 0: continue
#     else: print("Invalid Choice! Try Again")

# while True:
#     print("1. Tea\n2. Coffee\n3. Milkshake\n4. Lassi\n0. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice > 0 and choice <= 4: print("Good!")
#     elif choice == 0: break
#     else: print("Invalid Choice! Try Again")

# -------------------------------------------------

# for i in range(2, 21, 2):
#     print(i, end=", ")

# for _ in range(1, 20):
#     print("Hello, ")

# for i in range(-21, 2):
#     print(i)

# for i in range(1, 11):
#     print(11-i, end=", ")

# Palindrome Number/string

# -------------------------------------------------

totalPrice = 0

while True:
    print("1. Snacks")
    print("2. Beverages")
    print("0. Exit")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("1. Samosa - Rs.20")
            print("2. Kachori - Rs.20")
            print("3. Vadapav - Rs.45")
            print("4. Bhel - Rs.105")
            print("0. Exit")
            choice = int(input("Enter your choice: "))
            qty = int(input("Enter qty: "))

            match choice:
                case 1:
                    totalPrice += qty*20
                case 2:
                    totalPrice += qty*20
                case 3:
                    totalPrice += qty*45
                case 4:
                    totalPrice += qty*105
                case _:
                    print("Invalid snacks choice. Please try again!")

        case 2:
            print("1. MilkShake - Rs.50")
            print("2. Mocktail - Rs.120")
            print("3. Lassi - Rs.80")
            print("4. Cold Coffee - Rs.110")
            print("0. Exit")
            choice = int(input("Enter your choice: "))
            qty = int(input("Enter qty: "))

            match choice:
                case 1:
                    totalPrice += qty*50
                case 2:
                    totalPrice += qty*120
                case 3:
                    totalPrice += qty*80
                case 4:
                    totalPrice += qty*110
                case _:
                    print("Invalid beverage choice. Please try again!")

        case 0:
            print("Bill Summary:")
            print(f"Total Bill: {totalPrice}")
            print("Thanks for visiting us!")
            break

        case _:
            print("Invalid main choice! Please try again!")

