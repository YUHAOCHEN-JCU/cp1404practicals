"""
This program calculates total store item prices. It validates item numbers (rejecting <0),
accumulates item prices, applies a 10% discount for totals >$100,
and outputs the result with 2 decimal places.
"""

"""
DISCOUNT = 0.1

get number of items
while number of items < 0
    display error message
    get number of items
total price = 0
repeat i from 1 to number of items
    get price of item
    total price = total price + price of item
if total price > 100
    total price = total price - total price * DISCOUNT
display number of items, total price
"""

DISCOUNT = 0.1

# Get the valid number of items.
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items! ")
    number_of_items = int(input("Number of items: "))

# Calculate the total price.
total_price = 0
for i in range(number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
if total_price > 100:
    total_price = total_price - total_price * DISCOUNT
print(f"Total price for {number_of_items} items is ${total_price:.2f}  ")# Keep two decimal places.
