"""
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_PER_LINE = 6

get number_picks

repeat i in number_picks times
    quick_picks is empty list
    while length of quick_picks < NUMBER_PER_LINE
        number = random integer from MINIMUM_NUMBER to MAXIMUM_NUMBER
        if number not in quick_picks
            append number in quick_picks
        sort quick_picks
        print number in quick_picks
"""
import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBER_PER_LINE = 6

number_picks = int(input("How many quick picks? "))

for i in range(number_picks):
    quick_picks = []
    while len(quick_picks) < NUMBER_PER_LINE:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in quick_picks:
            quick_picks.append(number)
    quick_picks.sort()
    print(" ".join(f"{number:2}" for number in quick_picks))