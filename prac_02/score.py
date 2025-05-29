"""
CP1404/CP5632 - Practical
Broken program to determine score status, display level based on user input and random score.
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

function main()
    get score
    message = determine_level(score)
    display message
    random_score = generate_random_score()
    message = determine_level(random_score)
    display message


function determine_level(score)
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE
    return "Invalid score"
    else
        if score >= EXCELLENT_THRESHOLD
            return "Excellent"
        else if score >= PASS_THRESHOLD
            return "Passable"
        else
            return "Bad"


function generate_random_score()
    random_score = random choose a number from 0 to 100
    return random_score


main()
"""
from random import *

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50


def main():
    """Display level based on user input and random score"""
    score = float(input("Enter score: "))
    message = determine_level(score)
    print(message)
    random_score = generate_random_score()
    message = determine_level(random_score)
    print(message)


def determine_level(score):
    """Determine level based on score"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    else:
        if score >= EXCELLENT_THRESHOLD:
            return "Excellent"
        elif score >= PASS_THRESHOLD:
            return "Passable"
        else:
            return "Bad"


def generate_random_score():
    """Return random score"""
    random_score = randint(0, 100)
    return random_score


main()
