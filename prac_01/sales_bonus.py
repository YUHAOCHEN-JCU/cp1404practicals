"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""

CLASSIFICATION_SALES = 1000
LOW_DISCOUNT_RATE = 0.1
HIGH_DISCOUNT_RATE = 0.15

# Get sales based on user input, calculate bonus according to sales and print bonus.
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < CLASSIFICATION_SALES:
        bonus = sales * LOW_DISCOUNT_RATE
    else:
        bonus = sales * HIGH_DISCOUNT_RATE
    print(f"bonus: ${bonus}", sep="")
    sales = float(input("Enter sales: $"))
