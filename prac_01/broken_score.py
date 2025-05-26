"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
"""
get score
if score < 0 or score >100
    display error message
else if score > 90
    display "Excellent"
else if score > 50
    display"Passable"
else
    display"Bad"
"""
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50
message = ""

score = float(input("Enter score: "))

# Based on user input, determine the classification of the score and print the result.
if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
    print("Invalid score")
else:
    if score >= EXCELLENT_THRESHOLD:
        message = "Excellent"
    elif score >= PASS_THRESHOLD:
        message = "Passable"
    else:
        message = "Bad"
    print(message)
