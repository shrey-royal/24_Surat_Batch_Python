"""
# How to manually throw an exception
def calculateTotal(*prices: int):
    # print(prices, type(prices))
    for price in prices:
        if price < 1:
            raise ValueError("Price can't be negative.")
        
    return sum(prices)

totalPrice = 0
try:
    totalPrice = calculateTotal(1, 23, -12, 2134, 234, 23, 1, 1)
except ValueError as e:
    print(e)

print(f"Calculate Total: {totalPrice if totalPrice != 0 else "Error"}")
"""