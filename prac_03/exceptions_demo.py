"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
input is not a numeric type.
2. When will a ZeroDivisionError occur?
denominator equal to 0.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes.

try
    get numerator
    denominator = 0
    while denominator = 0
        get denominator
        if denominator = 0
            display error message
            get denominator
    fraction = numerator / denominator
    print fraction
except ValueError
    display error message
except ZeroDivisionError
    display error message
print "Finished"
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = 0
    while denominator == 0:
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Cannot divide by zero!")
            denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")