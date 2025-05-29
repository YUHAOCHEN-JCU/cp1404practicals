"""
MENU = ("(G)et a valid score (must be 0-100 inclusive)\n"
            "(P)rint result (copy or your function to determine the result from importscore.py))\n"
            "(S)how stars (this should print as many stars as the score)(Q)uit")
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

function main()
    display MENU
    get choice
    while choice not equal to "Q"
        if choice = "G"
            score = get_score()
            display score
        else if choice = "P"
            score = get_score()
            message = determine_level(score)
            display message
        else if choice == "S"
            score = get_score()
            number_of_star = print_star(score)
            display number_of_star
        else
            display error message
        display MENU
        get choice
    display "farewell"


function get_score()
    get score
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE
        display error message
        get score
    return score


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


function print_star(score)
    return "score" of "*"
"""
MENU = ("(G)et a valid score (must be 0-100 inclusive)\n"
            "(P)rint result (copy or your function to determine the result from importscore.py))\n"
            "(S)how stars (this should print as many stars as the score)(Q)uit")
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

def main():
    """display menu and do GPS based on user choice"""
    print(MENU)
    choice = input("Please enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
            print(f"OK! your score is {score}!")
        elif choice == "P":
            score = get_score()
            message = determine_level(score)
            print(message)
        elif choice == "S":
            score = get_score()
            number_of_star = print_star(score)
            print(number_of_star)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Please enter your choice: ").upper()
    print("farewell")


def get_score():
    """get user score based on user input"""
    score = float(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def determine_level(score):
    """determine level based on score"""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    else:
        if score >= EXCELLENT_THRESHOLD:
            return "Excellent"
        elif score >= PASS_THRESHOLD:
            return "Passable"
        else:
            return "Bad"


def print_star(score):
    """print star based on user score"""
    return int(score) * "*"


main()